"""
访谈
"""
from django.db import models
from account.models import UserRole, NewUser
from new_admin.models import ClassGrade


class Punish(models.Model):
    classes = models.ForeignKey(ClassGrade, on_delete=models.CASCADE, related_name='class_es')
    # 学生id
    student = models.ForeignKey(NewUser, on_delete=models.CASCADE, related_name='students')
    # 老师id
    teacher = models.ForeignKey(NewUser, on_delete=models.CASCADE, related_name='teachers')
    # 违纪内容
    violate_content = models.TextField()
    choice = (
        (1, '审请'),
        (2, '申请通过'),
        (3, '申请未通过')
    )
    # 审核状态
    state = models.PositiveSmallIntegerField(default=1, choices=choice)
    # 违纪处罚时间
    violate_date = models.DateField()
    # 申请（添加）时间
    apply_date = models.DateField(auto_now_add=True)
    # 审核时间
    check_date = models.DateField(null=True)
    choice_is = (
        (0, '正常'),
        (1, '删除')
    )
    # 删除状态字段
    is_del = models.PositiveSmallIntegerField(choices=choice_is, default=0)


class Inview(models.Model):
    classes = models.ForeignKey(ClassGrade, on_delete=models.CASCADE)
    student = models.ForeignKey(NewUser, on_delete=models.CASCADE, related_name='student')
    # 班主任
    teacher = models.ForeignKey(NewUser, on_delete=models.CASCADE, related_name='teacher')
    # 状态，是否删除
    choice = (
        (0, '正常'),
        (1, '删除')
    )
    state = models.IntegerField(choices=choice,default=0)
    # 处理方式
    handle = models.CharField(max_length=100)
    # 访谈内容
    content = models.TextField()
    # 处理结果
    result = models.CharField(max_length=20)
    # 访谈时间
    interview_date=models.DateField()
    # 访谈添加时间
    add_date = models.DateField(auto_now_add=True)
