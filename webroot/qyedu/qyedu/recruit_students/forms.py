from django import forms
from .models import Followup_state

class FollowForm(forms.ModelForm):
    class Meta:
        model = Followup_state
        fields = ['f_info']
        widgets = {
            'f_info': forms.Textarea(attrs={'class':'textarea','onkeyup':'$(this).Huitextarealength(this,200)','id':'info'}),
        }