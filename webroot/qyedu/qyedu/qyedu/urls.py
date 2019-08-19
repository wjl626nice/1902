"""qyedu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# coding=utf8
# from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    # 授课
    path('give_lessons/', include('give_lessons.urls')),
    # 后台
    path('new_admin/', include('new_admin.urls')),
    # 学习
    path('study/', include('study.urls')),
    # 人才库
    path('talent_all/', include('talent_all.urls')),
    # path('admin/', admin.site.urls),
    # 宿舍
    path('dormitory/', include("dormitory.urls")),
    # 考试
    path('examination/', include("examination.urls")),
    # 第三方模块验证码相关
    path('captcha/', include('captcha.urls')),
    # 招生
    path('recruit_students/', include('recruit_students.urls')),
    # 就业
    path('job/', include('obtain_employment.urls')),
    # 训练营
    path('star/', include('six_group.urls')),
    # 访谈
    path('interview/', include('interview.urls')),
    # 评测
    path('evaluate/', include('evaluate.urls')),

]


urlpatterns += [
    re_path(r'^media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}, name='media')
]