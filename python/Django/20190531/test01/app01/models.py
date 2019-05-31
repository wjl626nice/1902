from django.db import models

# Create your models here.
# 学生信息表
class Students(models.Model):
    id = models.AutoField(primary_key=True) # 创建一个自增的主键
    # 创建一个varchar(35)字段不为空的唯一（索引）字段
    student_names = models.CharField(max_length=35, null=False, unique=True)

    # 当对象被作为字符串输出时，会自动触发双下方法 __str__
    def __str__(self):
        return '<Students:<id-{},student_name-{}>>'.format(self.id, self.student_names)
# 班级表
# class Class(models.Model):
#     id = models.AutoField(primary_key=True)
#     class_name = models.CharField(max_length=35, null=False, unique=True)