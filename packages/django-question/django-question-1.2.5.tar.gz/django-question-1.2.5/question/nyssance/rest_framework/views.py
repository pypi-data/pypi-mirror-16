from base64 import b64encode
import datetime
import hashlib
import hmac
import json
import mimetypes
import os
import subprocess
from urllib.parse import quote_plus, urlparse
import uuid

from boto.s3.key import Key as S3Key
from django.conf import settings
from django.http.response import HttpResponse, HttpResponseBadRequest
import requests
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from nyssance.utils.func_ext import write_log

from ..django.db.utils import timestamp
from .response import ResponseBadRequest
from .serializers import DownloadUrlSerializer, UploadParamsSerializer
from nyssance.rest_framework.permissions import IsWhiteIpOrIsAuthenticated


def create_filename(filename):
    ext = filename.split('.')[-1]
    return '{}.{}'.format(uuid.uuid4().hex, ext)


def get_params(cloud, bucket, filename, rename, expiration, content_encoding, cache_control):
    content_type = mimetypes.guess_type(filename)[0] or S3Key.DefaultContentType
    path = 'upload/{}'.format(create_filename(filename)) if rename else filename  # 是否重命名.
    # 计算policy
    policy_object = {
        'expiration': (datetime.datetime.utcnow() + datetime.timedelta(hours=expiration)).strftime('%Y-%m-%dT%H:%M:%S.000Z'),
        'conditions': [
            {'bucket': bucket},
            ['starts-with', '$key', path.split('/')[0]],  # http://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-HTTPPOSTConstructPolicy.html
            ['starts-with', '$Content-Type', content_type]]}
    if cloud in ['aws', 's3']:
        policy_object['conditions'].append({'acl': 'public-read'})
        policy_object['conditions'].append({'success_action_status': '201'})  # 官方文档漏掉了, 这个在这里和html里一定不能少
        policy_object['conditions'].append(['content-length-range', 1, 1024 * 1024 * 4])
    if content_encoding == 'gzip':
        policy_object['conditions'].append(['starts-with', '$Content-Encoding', content_encoding])
    policy = b64encode(json.dumps(policy_object).replace('\n', '').replace('\r', '').encode())
    if settings.CLOUD_SECRET_ACCESS_KEY:  # 如果有SECRET.
        signature = b64encode(hmac.new(settings.CLOUD_SECRET_ACCESS_KEY.encode(), policy, hashlib.sha1).digest())
    else:
        signature_alg = os.path.join(settings.BASE_DIR, settings.CLOUD_SIGNATURE_FILE)
        signature = subprocess.check_output('{} --policy {}'.format(signature_alg, policy.decode()), shell=True).strip()
    # 返回params
    params = {'key': path,
              'Content-Type': content_type,
              'policy': policy.decode(),
              'signature': signature.decode()}
    if cloud in ['aliyun', 'oss']:
        params['OSSAccessKeyId'] = settings.CLOUD_ACCESS_KEY_ID
    elif cloud in ['aws', 's3']:
        params['AWSAccessKeyId'] = settings.CLOUD_ACCESS_KEY_ID
        params['acl'] = 'public-read'
        params['success_action_status'] = '201'
    if content_encoding == 'gzip':
        params['Content-Encoding'] = content_encoding
    if cache_control:
        params['Cache-Control'] = cache_control
    if bucket == settings.BUCKET_MEDIA:
        params['domain'] = 'https:{}'.format(settings.MEDIA_URL)
    elif bucket == settings.BUCKET_STATIC:
        params['domain'] = 'https:{}'.format(settings.STATIC_URL)
    elif bucket == settings.BUCKET_CLOUD:
        params['domain'] = 'https:{}'.format(settings.CLOUD_URL)
    return params


class DownloadUrlView(generics.RetrieveAPIView):
    """获取下载地址
    """
    serializer_class = DownloadUrlSerializer
#     permission_classes = IsOwner 需要权限自己才能看 FIXME

    def retrieve(self, request, *args, **kwargs):
        url = request.GET.get('url')  # http://test-documents-cmcaifu-com.oss-cn-hangzhou.aliyuncs.com/contract/001/Linux_Command3.pdf
        if not url:
            return ResponseBadRequest('url不能为空')
        url_components = urlparse(url)
        bucket = url_components.netloc.replace('.{}'.format(settings.CLOUD_STORAGE_BASE_DOMAIN), '')
        expires = int(timestamp(datetime.datetime.now())) + 600  # 10分钟有效.
        string_to_sign = 'GET\n\n\n{}\n/{}{}'.format(expires, bucket, url_components.path)  # 字符串.
        if settings.CLOUD_SECRET_ACCESS_KEY:  # 如果有SECRET.
            signature = b64encode(hmac.new(settings.CLOUD_SECRET_ACCESS_KEY.encode(), string_to_sign.encode(), hashlib.sha1).digest())
        else:
            signature_alg = os.path.join(settings.BASE_DIR, settings.CLOUD_SIGNATURE_FILE)
            signature = subprocess.check_output('{} --policy "{}"'.format(signature_alg, string_to_sign), shell=True).strip()  # 因为有换行符, 引号引起来.
        params = {'url': '{}?OSSAccessKeyId={}&Expires={}&Signature={}'.format(url, settings.CLOUD_ACCESS_KEY_ID, expires, quote_plus(signature))}
        return Response(params)


class UploadParamsView(generics.RetrieveAPIView):
    """获取上传参数
    filename -- 文件名, 可含有路径.
    expiration -- (可选)过期时间, 默认50年
    content_encoding -- (可选)默认不压缩
    cache_control -- (可选)默认没有
    """
    serializer_class = UploadParamsSerializer  # 加了只是为Swagger用, 不影响输出结果.
    permission_classes = (IsWhiteIpOrIsAuthenticated,)  # 本地调试用.

    def retrieve(self, request, *args, **kwargs):
        filename = request.GET.get('filename', '')
        bucket = request.GET.get('bucket', settings.BUCKET_MEDIA)
        if bucket == settings.BUCKET_MEDIA:  # 传到static下的不修改大小写
            filename = filename.lower()
        if filename == '':
            return ResponseBadRequest('filename不能为空')
        rename = False
        if bucket == settings.BUCKET_MEDIA:
            rename = True
        expiration = int(request.GET.get('expiration', 24 * 365 * 50))  # 过期时间.
        content_encoding = request.GET.get('content_encoding', '')
        cache_control = request.GET.get('cache_control')
        params = get_params(kwargs.get(self.lookup_field), bucket, filename, rename, expiration, content_encoding, cache_control)
        return Response(params)


class PaymentServiceCFCCallBackQuery(APIView):
    permission_classes = (AllowAny,)  # FIXME: 需要限定中金.

    def post(self, request, *args, **kwargs):
        write_log('payment_request', '{}'.format(self.trans_params(request)))
        headers = {'Content-Type': 'application/json'}
        url = '{}/notice'.format(settings.JAVA_API)
        result = requests.post(url, data=json.dumps(self.trans_params(request)), headers=headers).text
        write_log('payment_callback', '{}'.format(result))
        try:
            data = json.loads(result)
            return HttpResponse(data['content'])  # 去除双引号.
        except:
            return HttpResponseBadRequest(result)

    def trans_params(self, request):
        temp_dic = {}
        for k, v in request.data.items():
            if k:
                temp_dic[k] = v
        return temp_dic

download_url = DownloadUrlView.as_view()
upload_params = UploadParamsView.as_view()
payment_service_callback = PaymentServiceCFCCallBackQuery.as_view()
