from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from django.db import models


class Admin_user(ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username','email','date_joined')


class QyAuditing(models.Model):
    is_auditing = models.IntegerField('审核状态',default=0)

    class Meta:
        db_table = 'qy_auditing'

class AuditingSerializer(ModelSerializer):
    class Meta:
        model = QyAuditing
        fields = '__all__'