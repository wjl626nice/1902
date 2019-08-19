from django.urls import path
from . import views as admin_view


app_name = 'six_group'
urlpatterns = [
    # 训练营
    path('training_camp/', admin_view.training_camp, name='training_camp'),
    # 分配班级
    path('allocation_class/', admin_view.allocation_class, name='allocation_class'),
    # 分配班级验证
    path('allocation_class_check/', admin_view.allocation_class_check, name='allocation_class_check'),
    # 激活
    path('activate_state/', admin_view.activate_state, name='activate_state'),
    # 激活验证
    path('activate_state_check/', admin_view.activate_state_check, name='activate_state_check'),
    # 放弃
    path('activate_state_not/', admin_view.activate_state_not, name='activate_state_not'),
    # 普通班
    path('regular_class/',admin_view.regular_class, name='regular_class'),
    # 学生修改
    path('student_mod/', admin_view.student_mod, name='student_mod'),
    path('student_mod_check/', admin_view.student_mod_check, name='student_mod_check'),

    # 补贴
    path('subsidy/', admin_view.subsidy, name='subsidy'),
    path('subsidy_add/', admin_view.subsidy_add, name='subsidy_add'),
    path('subsidy_mod/', admin_view.subsidy_mod, name='subsidy_mod'),
    path('subsidy_add_check/', admin_view.subsidy_add_check, name='subsidy_add_check'),
    path('subsidy_mod_check/', admin_view.subsidy_mod_check, name='subsidy_mod_check'),
    # 住宿费
    path('dormitory/', admin_view.dormitory, name='dormitory'),
    # path('dormitory_add/', admin_view.dormitory_add, name='dormitory_add'),
    # 住宿费记录
    path('dormitory_record/', admin_view.dormitory_record, name='dormitory_record'),
    # 交易结算
    path('dormitory_close', admin_view.dormitory_close, name='dormitory_close'),
    # 财务删除
    path('remove_subsidy/', admin_view.remove_subsidy, name='remove_subsidy')
]
