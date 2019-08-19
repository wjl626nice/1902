from django.urls import path, include
from . import views as exam_views


app_name = 'examination'
urlpatterns = [
    # 考试记录
    path('record/info/', exam_views.record_info_list, name='record_info_list'),
    # 考试记录添加
    path('record/info/add', exam_views.record_info_add, name='record_info_add'),
    # 考试记录添加检测
    path('record/info/add/check', exam_views.record_info_add_check, name='record_info_add_check'),
    # 考试记录修改
    path('record/info/modify', exam_views.record_info_modify, name='record_info_modify'),
    # 考试记录修改检测
    path('record/info/modify/check', exam_views.record_info_modify_check, name='record_info_modify_check'),
    # 考试记录查询
    path('record/info/search', exam_views.record_search, name='record_search'),
    # 考试记录删除
    path('record/info/del/', exam_views.record_info_del, name='record_info_del'),
    #考试记录删除检测
    path('record/info/del/check/', exam_views.record_info_many_del, name='record_info_many_del'),
]
