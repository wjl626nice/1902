from django import forms

from evaluate.models import Answer


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_content', 'answer_score', 'question']
        widgets = {
            'answer_content': forms.TextInput(attrs={'id': "answer_content", 'name': "answer_content", 'class': "input-text",}),
            'answer_score': forms.TextInput(attrs={'id': "answer_score", 'name': "answer_score", 'class': "input-text", 'placeholder': '输入答案内容'}),
            'question': forms.Select(attrs={'id':'question', 'name':'question', 'class': 'select'})
        }
