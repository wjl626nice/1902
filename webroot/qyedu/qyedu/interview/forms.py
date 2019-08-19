from django import forms

from account.models import NewUser

from .models import Inview,Punish


class InterviewForm(forms.ModelForm):
    class Meta:
        model =Inview
        fields = [#"classes",
                  #"teacher",
                  "student","handle","content","result","interview_date"]
        widgets = {
            #"classes": forms.TextInput(attrs={'class': "input-text"}),
            # 'teacher':forms.Select(attrs={'class':'select','id':'teacher'}),
             'student':forms.Select(attrs={'class':'select','id':'student'}),
             "handle": forms.TextInput(attrs={'class': "input-text"}),
            "content": forms.Textarea(attrs={'class': "textarea"}),
            "result": forms.TextInput(attrs={'class': "result"}),
             'interview_date': forms.TextInput(attrs={'onfocus':"WdatePicker()",'class':"input-text Wdate" }),
        }


class PunishForm(forms.ModelForm):
    class Meta:
        model = Punish
        fields = [
            # "classes", "teacher",
            "student",
            "violate_content",
            "state"]
        widgets = {
            # "classes": forms.TextInput(attrs={'class': "input-text"}),
            #  'teacher':forms.Select(attrs={'class':'select','id':'teacher'}),
             'student':forms.Select(attrs={'class':'select','id':'student'}),
             # "handle": forms.TextInput(attrs={'class': "input-text"}),
            "violate_content": forms.Textarea(attrs={'class': "textarea"}),
            # "result": forms.TextInput(attrs={'class': "result"}),
             'violate_date': forms.TextInput(attrs={'class': "formControls col-xs-8 col-sm-9" }),
            'state': forms.Select(attrs={'class': 'select', 'id': 'states'}),

        }
