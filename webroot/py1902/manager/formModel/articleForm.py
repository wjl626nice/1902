from django import forms

# 验证文章表单
class ArticleForm(forms.Form):
    title = forms.CharField(label='标题', widget=forms.TextInput(attrs={"class":"input-text"}), required=True, max_length=150)
    tags = forms.CharField(label='标签', required=False)
    describles = forms.CharField(label='描述', required=False)
    seo_title = forms.CharField(label='seo标题', required=False)
    seo_keyword = forms.CharField(label='seo关键词', required=False)
    seo_description = forms.CharField(label='seo描述', required=False)
