from django.urls import path
from . import views as dorm_view

app_name = 'dormitory'
# 学员入住
urlpatterns = [
    # 学员入住信息
    path('dormstu/', dorm_view.dormstu_list, name="dormstu_list"),
    # 添加学员入住信息
    path('dormstu/add/', dorm_view.dormstu_add, name="dormstu_add"),
    # 添加入住学员验证
    path('dormstu/add_check/', dorm_view.dormstu_add_check, name="dormstu_add_check"),
    # 修改学员入住信息
    path('dormstu/modify/', dorm_view.dormstu_modify, name="dormstu_modify"),
    # 修改学员入住验证
    path('dormstu/modify_check/', dorm_view.dormstu_modify_check, name="dormstu_modify_check"),
    # 删除学生入住信息
    path('dormstu/delete/', dorm_view.dormstu_delete, name="dormstu_delete"),
]


# 宿舍问题处理
urlpatterns += [
    #宿舍问题处理页面
    path('problem/', dorm_view.stu_dorm_problem, name='stu_dorm_problem'),
    #宿舍问题添加
    path('problem/add/', dorm_view.pro_add, name='pro_add'),
    #宿舍问题添加检测
    path('problem/add/check/', dorm_view.pro_add_check, name='pro_add_check'),
    #宿舍问题编辑
    path('problem/modify/', dorm_view.pro_modify, name='pro_modify'),
    #宿舍问题编辑检测
    path('problem/modify/check/', dorm_view.pro_modify_check, name='pro_modify_check'),
    #宿舍问题删除
    path('problem/del/', dorm_view.pro_del, name='pro_del'),
    #问题已解决
    path('problem/resolve/', dorm_view.pro_resolve, name='pro_resolve'),
    #问题未解决
    path('problem/to/resolve/', dorm_view.pro_to_resolve, name='pro_to_resolve')
 ]
