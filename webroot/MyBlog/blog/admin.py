from django.contrib import admin
from blog.models import Category
from django.utils.safestring import mark_safe
# Register your models here.

# 注册模型类，然后在django自带管理后台展示
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'cate_name', 'pic_data', 'weight', 'num']

    # 控制执行操作显示的位置
    actions_on_top = False
    actions_on_bottom = True
    # 右侧过滤器
    list_filter = ['cate_name']
    # 控制搜索框，值是要搜索的字段
    search_fields = ['cate_name']
    list_editable = ['cate_name']
    # 设置只读字段
    readonly_fields = ['num']
    # 控制要修改的字段
    # fields = ['cate_name', 'pic']

    def pic_data(self, obj):
        return mark_safe("<img src='/%s' style='width:50px;height:50px;'>" % (obj.pic,))

    pic_data.short_description = 'aaaa'


# 注册模型类，然后在django自带管理后台展示
# admin.site.register(Category, CategoryAdmin)

# 网站头部标题
admin.site.site_header = 'Python1902博客管理系统'
# 设置网站标题
admin.site.site_title = 'Python1902博客管理系统'