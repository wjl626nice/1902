"""test02 URL Configuration

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
from django.urls import path
from django.shortcuts import HttpResponse
# 封装了uri对应的函数
# from test02.views import *
from .views import *

# uri的处理函数
def zh(request):
    return HttpResponse('张恒')
# uri 和 函数的映射

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('zh/', zh),
    # 登录展示uri
    path('logins', logins),
    # 检测登录的uri
    path('check_login', check_login),
    # 即展示登录页面，又检查登录
    path('login', login),
]
