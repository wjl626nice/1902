# coding=utf-8
from django.urls import path
from . import views as admin_view
from django.views.decorators.cache import cache_page
app_name = 'new_admin'

# 登录相关
urlpatterns = [
    # 首页
    path('', admin_view.index, name='index'),
    # 登录
    path('login/', admin_view.login, name='login'),
    # 登录验证
    path('login_check/', admin_view.login_check, name='login_check'),
    # 欢迎页
    path('welcome/', admin_view.welcome, name='welcome'),
    # 退出登录
    path('logout_view/', admin_view.logout_view, name='logout_view'),
]

# 菜单
urlpatterns += [
    # 栏目列表
    path('category/', admin_view.category, name='category'),
    # 栏目添加
    path('category/add/', admin_view.category_add, name='category_add'),
    # 栏目添加验证
    path('category/add/check/', admin_view.category_add_check, name='category_add_check'),
    # 删除栏目
    path('category/del/', admin_view.category_del, name='category_del'),
    # 修改栏目
    path('category/category_modify/', admin_view.category_modify, name='category_modify'),
    # 修改栏目验证
    path('category/category_modify/check/', admin_view.category_modify_check, name='category_modify_check'),
]

# 宿舍
urlpatterns += [
    # 宿舍列表
    path('dorm/', admin_view.dorm, name='dorm'),
    # 宿舍添加
    path('dorm/add/', admin_view.dorm_add, name='dorm_add'),
    # 宿舍添加验证
    path('dorm/add/check', admin_view.dorm_add_check, name='dorm_add_check'),
    # 宿舍修改
    path('dorm/modify/', admin_view.dorm_modify, name='dorm_modify'),
    # 宿舍修改验证
    path('dorm/modify/check', admin_view.dorm_modify_check, name='dorm_modify_check'),
    # 宿舍删除
    path('dorm/del/', admin_view.dorm_del, name='dorm_del'),
]

# 管理员管理
urlpatterns += [
    # 管理员列表
    path('admin/', admin_view.admin, name='admin'),
    # 管理员添加
    path('admin/add/check/', admin_view.admin_add_check, name='admin_add_check'),
    # 管理员添加验证
    path('admin/add/', admin_view.admin_add, name='admin_add'),
    # 删除管理员
    path('admin/del/', admin_view.admin_del, name='admin_del'),
    # 修改管理员
    path('admin/modify/', admin_view.admin_modify, name='admin_modify'),
    # 修改管理员验证
    path('admin/modify/check/', admin_view.admin_modify_check, name='admin_modify_check'),
    # 管理员启用
    path('admin/start/', admin_view.admin_start, name='admin_start'),
    # 管理员停用
    path('admin/stop/', admin_view.admin_stop, name='admin_stop'),
    # 修改密码
    path('admin/pwd_edit/', admin_view.admin_pwd_edit, name='admin_pwd_edit'),
]

# 班级管理
urlpatterns += [
    # 班级列表
    path('classgrade/', admin_view.classgrade, name='classgrade'),
    # 班级添加
    path('classgrade/add/', admin_view.classgrade_add, name='classgrade_add'),
    # 班级添加验证
    path('classgrade/add/check/', admin_view.classgrade_add_check, name='classgrade_add_check'),
    # 班级删除
    path('classgrade/del/', admin_view.classsgrade_del, name='classgrade_del'),
    # 班级修改
    path('classgrade/modify/', admin_view.classgrade_modify, name='classgrade_modify'),
    # 班级修改保存
    path('classgrade/save/', admin_view.classgrade_save, name='classgrade_save'),
    # 班级搜索
    path('classgrade/search/', admin_view.classgrade_search, name='classgrade_search'),
]

# 学员
urlpatterns += [
    # 学员管理
    path('student_list/', admin_view.student_list, name="student_list"),
    # 学员信息修改
    path('student_amend/', admin_view.student_amend, name="student_amend"),
    # 修改判断
    path('student_check/', admin_view.student_check, name="student_check"),
    # 学员删除
    path("student_delete/", admin_view.student_delete, name="student_delete"),
    # 学员搜索判断
    path("student_query/", admin_view.student_query, name="student_query"),
]
# 结业模块
urlpatterns +=[
    # 违纪，处罚页面
    path("violate_punish/", cache_page(10)(admin_view.violate_punish),name="violate_punish"),
    # 违纪，处罚判断
    path("violate_punish_ckeck/", admin_view.violate_punish_ckeck,name="violate_punish_ckeck"),
    # 补贴页面
    path("subsidy/", cache_page(10)(admin_view.subsidy), name="subsidy"),
    # 补贴搜索
    path("subsidy_ckeck/", admin_view.subsidy_ckeck,name="subsidy_ckeck"),
    # 技能成绩页面
    path("skill_grade/", cache_page(10)(admin_view.skill_grade),name="skill_grade"),
    # 技能成绩搜索判断
    path("skill_grade_ckeck/", admin_view.skill_grade_ckeck,name="skill_grade_ckeck"),
    # 职业素养页面
    path("profession_grade/", cache_page(10)(admin_view.profession_grade),name="profession_grade"),
    # 职业素养页面判断
    path("profession_grade_ckeck/", admin_view.profession_grade_ckeck,name="profession_grade_ckeck"),
    # 能力评估页面
    path("appraisal_report/", cache_page(10)(admin_view.appraisal_report),name="appraisal_report"),
    # 能力评估收搜页面
    path("appraisal_report_ckeck/", admin_view.appraisal_report_ckeck,name="appraisal_report_ckeck"),
    # 能力评估详细
    path("appraisal_detail/", admin_view.appraisal_detail,name="appraisal_detail"),
    # 访谈记录页面
    path("interview_record/", cache_page(10)(admin_view.interview_record),name="interview_record"),
    # 访谈记录收搜判断
    path("interview_record_ckeck/",admin_view.interview_record_ckeck,name="interview_record_ckeck")
]