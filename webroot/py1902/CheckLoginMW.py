from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect

class CheckLoginMW(MiddlewareMixin):
    def process_request(self, request):
        # 需要检查是否登录的uri
        verify_uris = ['/admin/index/']
        # 请求请求的uri
        current_uri = request.path_info
        if current_uri in verify_uris:
            # 判断是否登录
            if not request.session.get('user', ''):
                return redirect('/admin/login/')
