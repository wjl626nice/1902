# !/user/bin/env python
# !-*-coding:utf-8 -*-
# !@lime: 2018/12/3 8:37
# !@Author: fox
# !@File: urls.py
from django.urls import path
from . import views

app_name = 'give_lessons'
urlpatterns = [
    # 授课计划
    path('give_les/add/', views.giveles_add, name='giveles_add'),
    path('give_les/modify/', views.giveles_modify, name='giveles_modify'),
    path('give_les/modify/check/', views.giveles_modify_check, name='giveles_modify_check'),
    path('give_les/', views.giveles_show, name='giveles_show'),
    path('give_les/know/add/', views.know_add, name='know_add'),
    # 可选
    path('give_les/know/modify/', views.know_modify, name='know_modify'),
    path('give_les/know/modify/check/', views.know_modify_check, name='know_modify_check'),
    path('give_les/know/', views.know_show, name='know_show'),
]