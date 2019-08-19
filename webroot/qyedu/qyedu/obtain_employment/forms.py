from django.forms import ModelForm
from django import forms
from .models import Enterprise


class EnterpriseForm(ModelForm):
    class Meta:
        model = Enterprise
        exclude = ['add_time']
        widgets = {
            'e_name': forms.TextInput(attrs={'class':'input-text'}),
            'e_address':forms.TextInput(attrs={'class':'input-text'}),
            'e_contact': forms.TextInput(attrs={'class': 'input-text'}),
            'e_contact_phone': forms.TextInput(attrs={'class': 'input-text', 'maxlength':11}),
            'e_prtocol': forms.ClearableFileInput(attrs={'class': 'input-file', 'id':'uploadfile','style':'width:200px'}),

        }

