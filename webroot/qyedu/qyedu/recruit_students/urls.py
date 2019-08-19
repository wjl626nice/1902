from django.urls import path
from . import views

app_name = 'recruit_students'
urlpatterns = [
    # 跟进状态
    path('followup_state/',views.followup_state,name='followup_state'),
    # 跟进状态记录添加
    path('followup_add/', views.followup_add,name='followup_add'),
    # 跟进状态保存
    path('followup_save/',views.followup_save,name='followup_save'),
    # 跟进状态编辑
    path('followup_edit/',views.followup_edit,name='followup_edit'),
    # 跟进状态编辑保存
    path('followup_edit_save/',views.followup_edit_save,name='followup_edit_save'),
    # 跟进状态删除
    path('followup_del/',views.followup_del,name='followup_del'),
    # 跟进状态搜索
    path('followup_search/',views.followup_search,name='followup_search'),

    # 生源录入
    path('input/', views.input, name='input'),
    # 生源添加
    path('add/',views.add_students,name='add_students'),
    # 生源添加验证
    path('add/check/',views.add_students_check,name='add_students_check'),
    # 生源删除
    path('del/', views.del_student,name='del_student'),
    # 生源信息修改
    path('modify/', views.modify_student,name='modify_student'),
    # 生源信息修改验证
    path('modify/check/', views.student_modify_check,name='student_modify_check'),
    # 生源信息搜索
    path('search/', views.student_search,name='student_search'),
    # 生源分发页面
    path('distribution/', views.students_distribute, name='students_distribute'),
    path('distribution/to_person/', views.dis_to_person, name='dis_to_person'),
]