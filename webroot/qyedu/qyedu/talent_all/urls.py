# !/user/bin/env python
# !-*-coding:utf-8 -*-
# !@lime: 2018/12/3 8:38
# !@Author: fox
# !@File: urls.py
from django.urls import path, re_path
from . import views

app_name = 'talent'
urlpatterns = [
    # 人才库
    path('talent_list/', views.talent_list, name='talent_list'),
    path('talent/delete/', views.talent_delete, name='talent_delete'),
    # 标签列表
    path('tag/', views.tag_add, name='tag_add'),
    path('tag/delete/', views.tag_delete, name='tag_delete'),
    path('tag/save/', views.tag_save, name='tag_save'),
    path('tag/save_to/', views.tag_save_to, name='tag_save_to'),
    path('tag_list/', views.tag_list, name='tag_list'),
    path('tag/show/', views.tag_show, name='tag_show'),
    # 人才查询
    path('talent/student_query/', views.student_query, name='student_query'),
    path('talent/tag_query/', views.tag_query, name='tag_query'),
]
