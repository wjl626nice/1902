from django.urls import path,re_path
from .import views

app_name = 'job'
urlpatterns = [

    # 展示已添加的就业记录
    path('work_records/', views.work_records,name='work_records'),
    # 展示已毕业学生
    path('graduate/', views.graduate,name='graduate'),
    #添加记录
    re_path(r'^add_records/(?P<id>\d+)/$', views.add_records,name='add_records'),
    #添加记录验证
    path('add_records_check/',views.add_records_check,name='add_records_check'),
    #修改记录
    re_path('^change_records/(?P<id>\d+)/$',views.change_records,name='change_records'),
    #修改纪录认证
    path('change_records/check/',views.change_records_check,name='change_records_check'),
    #删除记录
    path('delete_records/',views.delete_records,name='delete_record'),
    #权限验证
    path('add_yan/',views.add_yan,name='add_yan'),
    #搜索
    path('records_search/',views.records_search,name='records_search'),
    #展示记录
    path('visited_recordes/', views.visited, name='visited'),
    #添加回访记录
    re_path(r'^visited_recordes/(?P<id>\d+)/$', views.visited_add, name='visited_add'),
    #添加回访记录认证
    path('visited_add_check/',views.visited_add_check,name='visited_add_check'),
    #修改回访记录
    re_path(r'^visited_modify/(?P<id>\d+)/$',views.visited_modify,name='visited_modify'),
    #修改回访记录认证
    path('visited_modify_check/', views.visited_modify_check, name='visited_modify_check'),
    #展示已就业学生列表
    path('job_students/',views.job_students,name='job_students'),
    #删除回访记录
    path('delete_visited/',views.delete_visited,name='delete_visited'),
    #回访记录搜索
    path('search_visited/',views.search_visited,name='search_visited'),
    # 企业列表
    path('enterprise/', views.enterprise, name='enterprise'),
    # 添加企业
    path('enterprise/add/',views.enterprise_add, name='enterprise_add'),
    # 企业添加验证
    path('enterprise/check/', views.enterprise_check, name='enterprise_check'),
    # 企业修改
    path('enterprise/modify/', views.enterprise_modify, name='enterprise_modify'),
    # 企业修改验证
    path('enterprise/modify/check/', views.enterprise_modify_check,name='enterprise_modify_check'),
    # 企业删除
    path('enterprise/del/', views.enterprise_del, name='enterprise_del'),
]
