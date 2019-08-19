from django.urls import path
from . import views


app_name = 'interview'

urlpatterns = [
    # 访谈记录展示
    path('interview_show/',views.interview_show,name='interview_show'),
    # 访谈主页
    # path('interview_index', views.index,name='index'),
    # 添加访谈记录
    path('interview_add/', views.interview_add, name='interview_add'),
    # 添加访谈记录验证
    path('interview_add_check/',views.interview_add_check,name='interview_add_check'),
    # 修改访谈记录
    path('interview_modify/', views.interview_modify, name='interview_modify'),
    # 修改后保存访谈记录
    path('interview_save/',views.interview_save,name='interview_save'),
    # 访谈搜索
    path('interview_search_check/',views.interview_search_check,name='interview_search_check'),
    # 删除访谈记录
    path('interview_del/',views.interview_del,name='interview_del'),
    # 违纪处罚页面展示
    path('punish_show_manage/', views.punish_show_manage, name='punish_show_manage'),
    # 违纪处罚表搜索
    path('punish_search_ckeck/', views.punish_search_ckeck, name='punish_search_ckeck'),
    # path('punish_show/',views.punish_show,name='punish_show'),
    # 申请（添加）违纪处罚记录
    path('punish_add/',views.punish_add,name='punish_add'),
    # 申请(添加）违纪处罚验证
    path('punish_add_check/',views.punish_add_check,name='punish_add_check'),
    # 删除违纪处罚记录
    path('punish_del/', views.punish_del,name='punish_del'),
    # 修改违纪处罚记录
    path('punish_modify/', views.punish_modify,name='punish_modify'),
    # 修改违纪处罚验证
    path('punish_save/', views.punish_save,name='punish_save'),




]