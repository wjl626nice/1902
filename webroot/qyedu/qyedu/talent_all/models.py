"""
人才库
"""

from django.db import models
from account.models import NewUser

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=20)
    Recruiter_id = models.ForeignKey(NewUser, on_delete=models.DO_NOTHING)
    is_del = models.IntegerField(default=0)

    class Meta:
        db_table = 'tag'

    def __str__(self):
        return self.name


class Talent(models.Model):
    tags = models.ManyToManyField(Tag, related_name='tag')
    add_date = models.DateTimeField(auto_now_add=True)
    student_id = models.OneToOneField(NewUser, on_delete=models.CASCADE, related_name='stu_a')
    Recruiter_id = models.ForeignKey(NewUser,on_delete=models.DO_NOTHING, related_name='rec_a')
    is_del = models.IntegerField(default=0)

    class Meta:
        db_table = 'talent'
