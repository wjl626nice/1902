"""test01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('abc', views.abc),

    path('add_book', views.add_book),
    # 基于视图（类）的uri映射方法
    path('add_books', views.add_books.as_view()), # 可以自动根据http请求方法，调用类内的get post请求
    # 测试请求对象的属性
    path('request_attr', views.get_attr_by_request),
    # 测试上传图片
    path('upload_file', views.upload_file),
    # 测试请求对象的方法
    path('request_method', views.request_method),
    # 测试响应对象
    path('get_response', views.get_response),
    # 测试ajax请求
    path('test_ajax', views.test_ajax),
    # 测试响应结果
    path('response_json', views.response_json),
    # 测试 render
    path('get_render', views.get_render),
    # 测试重定向
    path('get_red', views.get_redirect),
]
