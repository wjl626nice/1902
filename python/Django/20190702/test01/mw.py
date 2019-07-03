from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect

class mw1(MiddlewareMixin):
    def process_request(self, request):
        """
        在路由前自动执行
        :param request:
        :return:
        """
        # 白名单
        whiteList = ['/admin/index/', '/admin/category/', '/admin/article/', '/admin/article_add/']
        uri = request.path_info
        # uri1 = request.get_full_path_info()
        # 判断是否在白名单中。
        if uri in whiteList:
            pass
        else:
            pass
            # 判断是否登录
            # if not request.session.get('is_login'):
            #     # 跳转到登录页面
            #     return redirect('/login')

        print('来了,老弟1')
        # return HttpResponse('')

    def process_response(self, request, response):
        """
        在视图处理以后自动执行
        :param request:
        :param response:
        :return:
        """
        print('走了，老弟1!')
        response.content = response.content + 'abcs2'.encode()
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        在路由之后，视图执行之前执行
        :param request:
        :param view_func:
        :param view_args:
        :param view_kwargs:
        :return:
        """
        print('*' * 80)
        print('mw1中间件的process_view方法')
        print(view_func, view_args, view_kwargs)
    def process_exception(self, request, exception):
        """
        views中有异常抛出时 自动执行
        :param request:
        :param exception:
        :return:
        """
        print(exception)
        print('mw1中间件的process_exception方法')
        # 自定义输出内容
        return HttpResponse('可能错误！')


"""
 process_request-->urls.py--->process_view--->view.py--->没异常 process_response
                                                     --->有异常 process_exception ---->process_response
"""


class mw2(MiddlewareMixin):
    def process_request(self, request):
        """
        在路由前自动执行
        :param request:
        :return:
        """
        print('来了,老弟2')
        # return HttpResponse('')

    def process_response(self, request, response):
        """
        在视图处理以后自动执行
        :param request:
        :param response:
        :return:
        """
        print('走了，老弟2!')
        response.content = response.content + 'abcs2'.encode()
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        在路由之后，视图执行之前执行
        :param request:
        :param view_func:
        :param view_args:
        :param view_kwargs:
        :return:
        """
        print('*' * 80)
        print('mw2中间件的process_view方法')
        print(view_func, view_args, view_kwargs)
    def process_exception(self, request, exception):
        """
        views中有异常抛出时 自动执行
        :param request:
        :param exception:
        :return:
        """
        print(exception)
        print('mw2中间件的process_exception方法')
        # 自定义输出内容
        return HttpResponse('可能错误！')