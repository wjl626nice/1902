from django.db import models
from django.utils import timezone
from account.models import UserRole, NewUser


class Menu(models.Model):
    """
    菜单表
    """
    menu_name = models.CharField(max_length=20)
    page_url = models.CharField(max_length=100)
    parent_id = models.IntegerField(default=0)
    role = models.ManyToManyField(UserRole)
    is_del = models.IntegerField(default=0)

    def __str__(self):
        return self.menu_name


class ClassGrade(models.Model):
    """
    班级表
    """
    classname = models.CharField(max_length=20)
    add_user = models.ForeignKey(NewUser, on_delete=models.DO_NOTHING, related_name='add_user')
    state = models.IntegerField(default=0)
    add_time = models.DateTimeField(default=timezone.now)
    teacher_user = models.ForeignKey(NewUser, on_delete=models.DO_NOTHING, related_name='teacher_user')
    manager_user = models.ForeignKey(NewUser, on_delete=models.DO_NOTHING, related_name='manager_user')
    start_time = models.DateField(null=True)
    end_time = models.DateField(null=True)
    choice = (
        (0,'训练营'),
        (1,'普通班级')
    )
    class_type = models.PositiveSmallIntegerField(choices=choice,default=0)

    def __str__(self):
        return self.classname

# 宿舍
class Dorm(models.Model):
    """
    宿舍表
    """
    dorm_name = models.CharField(max_length=20)
    add_user = models.ForeignKey(NewUser, models.DO_NOTHING)
    add_time = models.DateTimeField(default=timezone.now)
    max_stu = models.IntegerField()
    is_del = models.IntegerField(default=0)

    def __str__(self):
        return self.dorm_name

# 班级学生
class StuClass(models.Model):
    # 班级
    grade = models.ForeignKey(ClassGrade,on_delete=models.DO_NOTHING, related_name='stuclass_grade')
    # 学生
    student = models.ForeignKey(NewUser,on_delete=models.DO_NOTHING, related_name='stuclass_student')
    # 录入人
    keyboarder = models.ForeignKey(NewUser,on_delete=models.DO_NOTHING, related_name='stuclass_keyboarder')
    # 录入时间
    add_time = models.DateField(auto_now_add=True)


# 财务表
class Subsidy(models.Model):
    # 金额
    money = models.IntegerField()
    type_chose = ((1, '补贴'), (2, '住宿费'))
    # 金额类型
    type = models.PositiveSmallIntegerField(default=1, choices=type_chose)
    # 录入时间
    data_time = models.DateTimeField(auto_now=True)
    # 缴费或补贴时间
    pay_time = models.DateField(null=True)
    # 缴纳学生
    student = models.ForeignKey(NewUser, on_delete=models.CASCADE, related_name='subsidys')
    # 录入人
    keyboarder = models.ForeignKey(NewUser, on_delete=models.CASCADE, related_name='subsidyes')
    choice_state = ((1,'已结算'), (0, '未结算'))
    # 是否结算
    state = models.PositiveSmallIntegerField(choices=choice_state, default=0)
    # 结算时间
    close_time = models.DateTimeField(auto_now=True)
