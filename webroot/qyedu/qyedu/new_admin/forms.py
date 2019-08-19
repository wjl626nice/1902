from django import forms
from captcha.fields import CaptchaField
from django.forms import ModelForm
from account.models import User
from .models import NewUser
from new_admin.models import ClassGrade

from new_admin.models import ClassGrade


class UserForm(forms.Form):
    captcha = CaptchaField(label='验证码')


# 管理员表单NewUser
class RoleForm(ModelForm):
    class Meta:
        model = NewUser
        fields = ['user', 'realname', 'gender', 'mobile_number', 'id_card', 'birthday', 'info', 'edu_level', 'home_address', 'role']


# 用户管理表单
class UserStaffForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'is_staff']


class ClassGradeForm(forms.ModelForm):
    class Meta:
        model = ClassGrade
        fields = ['classname','start_time','end_time','manager_user','teacher_user','class_type']
        widgets = {
            'classname':forms.TextInput(attrs={'class':'input-text','id':'classname'}),
            'start_time':forms.TextInput(attrs={'onfocus':"WdatePicker()", 'id':"logmin", 'name':"start_time" ,'class':"input-text Wdate", 'style':"width:552.500px;" ,'autocomplete':"off"}),
            'end_time':forms.TextInput(attrs={'onfocus':"WdatePicker()", 'id':"logmax", 'class':"input-text Wdate" ,'style':"width:552.500px;" ,'autocomplete':"off",}),
            'manager_user':forms.Select(attrs={'class':'select','id':'manager_user'}),
            'teacher_user':forms.Select(attrs={'class':'select','id':'teacher_user'}),
            'class_type':forms.Select(attrs={'class': "input-text"})
        }

    def __init__(self, *args, **kwargs):
        super(ClassGradeForm, self).__init__(*args, **kwargs)
        self.fields['start_time'].required = False
        self.fields['end_time'].required = False


# 学员修改信息form表单
class NewUserForm(forms.ModelForm):
    class Meta:
        model = NewUser
        fields = ["realname", "mobile_number","id_card","birthday","info","gender","edu_level","home_address","state","is_goodman"]
        widgets = {
            "realname": forms.TextInput(attrs={'class': "input-text"}),
            "mobile_number": forms.TextInput(attrs={'class': "input-text","id":"telephone"}),
            "id_card": forms.TextInput(attrs={'class': "input-text","id":"identity"}),
            "birthday": forms.DateInput(attrs={'onfocus':"WdatePicker()",'class': "input-text Wdate","id":"commentdatemin"}),
            "info": forms.Textarea(attrs={'class': "textarea"}),
            "gender": forms.Select(attrs={'class': "input-text"}),
            "edu_level": forms.TextInput(attrs={'class': "input-text"}),
            "home_address": forms.TextInput(attrs={'class': "input-text"}),
            "state": forms.Select(attrs={'class': "input-text"}),
            "is_goodman": forms.Select(attrs={'class': "input-text"}),
        }


