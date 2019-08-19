# coding=utf8

from django.urls import path, re_path
from . import views

app_name = 'study'
urlpatterns = [
    path('main/', views.stu_main, name='stu_main'),
    path('a/<str:id_juge>', views.student_sign,name='student_sign'),
    path('sign/', views.stu_sign, name='stu_sign'),
    path('sign/add/', views.stu_add, name='stu_add'),
    path('self/show/', views.self_show, name='self_show'),
    path('qian/selfshow/', views.qian_selfshow, name='qian_selfshow'),
    path('self/add/', views.self_add, name='self_add'),
    path('self/modify/', views.self_modify, name='self_modify'),
    path('stuweek/add/', views.stuweek_add, name='stuweek_add'),
    path('qianweek/', views.qianweek, name='qianweek'),
    # path('qianweek/modify/', views.qianweek_modify, name='qianweek_modify'),
    path('stuweek/show/', views.stuweek_show, name='stuweek_show'),
    path('stuweek/modify/', views.stuweek_modify, name='stuweek_modify'),
]