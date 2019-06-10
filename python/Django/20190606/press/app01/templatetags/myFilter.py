from django import template

# 实例化Django模型引擎的库类
register = template.Library()

# 通过装饰器 注册自定义过滤器，name 在模板中使用的过滤器名字。
@register.filter(name="aabb")
def abc(value):
    return value + '你真帅！'

@register.filter(name="rp")
def rp(value, search):
    # 把字符串拆分成列表，解决多参问题
    args = search.split(',')
    return value.replace(args[0], args[1])
