"""
测评、职业素养
"""
from django.db import models
from new_admin.models import *


# Create your models here.
class ReviewTest(models.Model):
    """
    考试记录表(考试对象是学生)
    """
    # 学生所在班级
    class_grade = models.ForeignKey(ClassGrade,on_delete=models.CASCADE, related_name='rt_class_grade')
    # 评测对象--老师/职业素养课--老师
    teacher_name = models.ForeignKey(NewUser, models.DO_NOTHING, related_name='rt_teacher_name')
    # 本次测试名称
    test_name = models.CharField(max_length=15)
    # 测试时间
    review_test_date = models.DateTimeField()
    # 是否允许考试(默认为0)
    can_test = models.BooleanField(default=0)

    def __str__(self):
        return self.test_name


class TestQuestion(models.Model):
    """
    问题库(测试问题表)
    """
    # 外键 -- 评测表
    review_test = models.ForeignKey(ReviewTest, on_delete=models.DO_NOTHING,related_name='tq_review_test')
    test_categoty_choices = (
        (1, '讲师评测'),
        (2, '班主任评测'),
        (3, '后勤评测'),
        (4, '职业素养测评'),
    )
    # 测试--类型
    test_category = models.SmallIntegerField(choices=test_categoty_choices, default=1)
    test_question_categoty_choices = (
        (1, '单选题'),
        (2, '是非题'),
        (3, '主观题')
    )
    # 测试题目类型
    test_question_category = models.SmallIntegerField(choices=test_question_categoty_choices, default=1)
    # 最大分数(主要针对主观题, 默认10分)
    max_score = models.IntegerField(default=10)
    # 测试题目内容
    test_question_content = models.CharField(max_length=200)

    def __str__(self):
        return self.test_question_content


class Answer(models.Model):
    """
    答案库(问题答案表)
    """
    # 外键--问题
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE, related_name='a_question')
    # 答案内容
    answer_content = models.CharField(max_length=500)
    # 每个答案所对应的分数
    answer_score = models.IntegerField(default=0)

    def __str__(self):
        return self.answer_content


class StudentAnswer(models.Model):
    """
    学生答案表
    """
    # 考试记录
    review_test = models.ForeignKey(ReviewTest, on_delete=models.DO_NOTHING, related_name='sa_review_test')
    # 试卷问题
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE, related_name='sa_question')
    # 答案(选择题为选项, 简答题为内容)
    answer = models.CharField(max_length=500)
    # 考试人
    student = models.ForeignKey(NewUser, on_delete=models.CASCADE, related_name='sa_student')
    # 交卷时间
    submit_time = models.DateTimeField(auto_now_add=True)


class ReviewResult(models.Model):
    """
    测评结果--成绩表
    """
    # 测试名称
    review_test = models.ForeignKey(ReviewTest, on_delete=models.DO_NOTHING, related_name='r_review_test')
    # 测试人
    student = models.ForeignKey(NewUser, on_delete=models.CASCADE, related_name='r_student')

    # 测试类型
    test_category = models.CharField(max_length=20)
    # 测试总分数(缺考为-1)
    review_test_score = models.IntegerField(default=-1)


# 职业素养课表
class Course(models.Model):
    name = models.CharField(max_length=20)
    outline = models.TextField(max_length=300)
    demand = models.TextField(max_length=300)
    open_time = models.DateTimeField()
    add_time = models.DateTimeField(auto_now_add=True)
