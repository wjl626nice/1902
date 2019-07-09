from django import forms

# 验证栏目表单
class CategoryForm(forms.Form):
    cate_name = forms.CharField(label="栏目名称", widget=forms.TextInput(attrs={"class": "input-text", "id": "aaaaaa"}), required=True, min_length=2)
    describles = forms.CharField(label="描述", required=False)
    is_menu = forms.BooleanField(label='是否是菜单', required=False)
    weight = forms.IntegerField(label='权重（越大越靠前）', required=False, error_messages={
        "invalid": '格式不正确！'
    })
    pic = forms.ImageField(label="图片", required=False)
    seo_title = forms.CharField(label="seo标题", required=False)
    seo_keyword = forms.CharField(label="seo关键词", required=False)
    seo_description = forms.CharField(label="seo描述", required=False)
