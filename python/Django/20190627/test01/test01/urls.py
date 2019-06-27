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
from django.urls import path, include
from app01.views import *
from app01.viewss import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('abc/', abc),
    path('aaa/', aaa),
    path('login/', login),
    path('checkLogin/', checkLogin),
    path('index/', index),
    path('article/', article),
    path('loginOut/', loginOut),

    path('aaa/a/b/', aaa_a_b),
    path('aaa/a/b/c/', aaa_a_b_c),
    path('aaa/a/', aaa_a),

    # 为了二级域名(wz.dongyang.com)设置url
    path('wazi', wazi),
    path('wazi_gc', wazi_gc),

    # 为了二级域名(x.dongyang.com)设置url
    path('x_gc', x_gc),


    # 测试session
    path('app02/', include('app02.urls'))

]
