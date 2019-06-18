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
from django.urls import path, re_path, include
from app01.views import *
from sysAdmin.views import *
from django.conf import settings


urlpatterns = [
    # 精准路由
    # path('admin/', admin.site.urls),
    path('home/', home),
    path('pingguo/s14', pingguos),
    # 地址转换路由
    path('pingguo/s<int:id>', pingguoss, {'abc': '坏苹果'}, name="lpg"),  # pingguo/s11
    path('pingguos/<str:area>/s<int:id>', pingguoss, name="hpg"),  # pingguo/zhongning/s31
    path('news/<int:year>/', news_list),  # news/2019/
    path('news/<int:year>/<int:month>.html', news_list),  # news/2019/3.html
    path('news/<int:year>/<int:month>/<int:id>.html', news_show),  # news/2019/5/23.html
    # 正则路由
    re_path(r'^$', home),
    re_path(r'^banana/s(\d+)$', banana_type),
    #  banana/zhongning/s11
    re_path(r'^banana/([a-z]+)/s(\d+)$', banana_types),
    #  banana/2017|1017/      # 未命名分组
    re_path(r'^banana/([12]\d{3})/$', banana_lists),
    #  banana/2019/33.html    # 命名分组
    re_path(r'^banana/(?P<year>[12]\d{3})/(?P<month>\d{1,2}).html', banana_listss),

    # 定义包含路由
    # path('admin/login/', login)
    path('admin/', include('sysAdmin.urls')),
    path('member/', include('member.urls')),
]
