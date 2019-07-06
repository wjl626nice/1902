from django import forms

# 验证栏目表单
class CategoryForm(forms.Form):
    cate_name = forms.CharField(label="栏目名称", widget=forms.TextInput(attrs={"class": "input-text", "id": "aaaaaa"}), required=True, min_length=2)
    describles = forms.CharField(label="描述", required=False)
    pic = forms.ImageField(label="图片", required=False)
    seo_title = forms.CharField(label="seo标题", required=False)
    seo_keyword = forms.CharField(label="seo关键词", required=False)
    seo_description = forms.CharField(label="seo描述", required=False)
