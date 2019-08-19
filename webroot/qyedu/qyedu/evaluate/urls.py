from django.urls import path
from . import views as evaluate_view


app_name = 'evaluate'
# 考试信息
urlpatterns = [
    # 进入录入考试的页面
    path('evaluate_test/add', evaluate_view.evaluate_test_add, name='evaluate_test_add'),
    # 添加哪场考试
    path('evaluate_test/add/check', evaluate_view.evaluate_test_add_check, name='evaluate_test_add_check'),
    # 展示考试信息页面
    path('evaluate_test/show/', evaluate_view.evaluate_test_show, name='evaluate_test_show'),
    # 修改考试信息
    path('evaluate_test/modify/', evaluate_view.evaluate_test_modify, name='evaluate_test_modify'),
    path('evaluate_test/modify/check/', evaluate_view.evaluate_test_modify_check, name='evaluate_test_modify_check'),
    # 删除考试信息
    path('evaluate_test/delete/', evaluate_view.evaluate_test_delete, name='evaluate_test_delete')

]

# 题库
urlpatterns += [
    # 录入考题页面
    path('evaluate_test/question/', evaluate_view.evaluate_test_question, name='evaluate_test_question'),
    # 添加考题
    path('evaluate_test/question/add/', evaluate_view.evaluate_test_question_add, name='evaluate_test_question_add'),
    path('evaluate_test/question/add/check/', evaluate_view.evaluate_test_question_add_check, name='evaluate_test_question_add_check'),
    # 修改考题
    path('evaluate_test/question/modify/', evaluate_view.evaluate_test_question_modify, name='evaluate_test_question_modify'),
    path('evaluate_test/question/modify/check', evaluate_view.evaluate_test_question_modify_check, name='evaluate_test_question_modify_check'),
    # 删除考题
    path('evaluate_test/question/delete/', evaluate_view.evaluate_question_delete, name='evaluate_question_delete'),
]

# 答案库
urlpatterns += [

    # 录入答案页面
    path('evaluate_test/answer/', evaluate_view.evaluate_test_answer, name='evaluate_test_answer'),
    # 添加答案页面
    path('evaluate_test/answer/add/', evaluate_view.evaluate_test_answer_add, name='evaluate_test_answer_add'),
    # 添加答案
    path('evaluate_test/answer/add/check/', evaluate_view.evaluate_test_answer_add_check, name='evaluate_test_answer_add_check'),


    # 修改答案页面
    path('evaluate_test/answer/modify/', evaluate_view.evaluate_test_answer_modify, name='evaluate_test_answer_modify'),
    # 修改答案
    path('evaluate_test/answer/modify/check/', evaluate_view.evaluate_test_answer_modify_check, name='evaluate_test_answer_modify_check'),

    # 删除答案
    path('evaluate_test/answer/delete/', evaluate_view.evaluate_test_answer_delete, name='evaluate_test_answer_delete'),

]

# 职业素养课考试
urlpatterns += [
    path('evaluate_course_test/show/', evaluate_view.evaluate_course_test_show, name="evaluate_course_test_show"),
    path('evaluate_course_test/submit/', evaluate_view.evaluate_course_test_submit, name='evaluate_course_test_submit'),
    path('evaluate_course_test_answer/', evaluate_view.evaluate_course_test_answer, name='evaluate_course_test_answer'),
]

# 讲师评测
urlpatterns += [
    # 展示考题
    path('evaluate_teacher_test/', evaluate_view.evaluate_teacher_test, name='evaluate_teacher_test'),
    # 提交考题
    path('evaluate_teacher_test/submit/', evaluate_view.evaluate_teacher_test_submit, name='evaluate_teacher_test_submit'),
    # 考试答案,及批阅
    path('evaluate_student_answer/', evaluate_view.evaluate_student_answer, name='evaluate_student_answer')
]

# 班主任评测
urlpatterns += [
    # 展示考题
    path('evaluate_headteacher_test/', evaluate_view.evaluate_headteacher_test, name='evaluate_headteacher_test'),
    # 提交考题
    path('evaluate_headteacher_test/submit/', evaluate_view.evaluate_headteacher_test_submit, name='evaluate_headteacher_test_submit'),
    # 考试答案, 及批阅
    path('evaluate_headteacher_test/answer/', evaluate_view.evaluate_headteacher_test_answer, name='evaluate_headteacher_test_answer'),
    # ajax-获取总成绩并保存
    path('evaluate_headteacher_test/sum/', evaluate_view.evaluate_headteacher_test_sum, name='evaluate_headteacher_test_sum'),


]


# 后勤服务评测
urlpatterns += [
    # 展示考题
    path('evaluate_service_test/', evaluate_view.evaluate_service_test, name='evaluate_service_test'),
    # 提交考题
    path('evaluate_service_test/submit/', evaluate_view.evaluate_service_test_submit, name='evaluate_service_test_submit'),
    # 考试答案
    path('evaluate_service_test/answer/', evaluate_view.evaluate_service_test_answer, name='evaluate_service_test_answer'),
]

