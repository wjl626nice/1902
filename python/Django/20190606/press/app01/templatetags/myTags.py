from django import template

register = template.Library()

@register.simple_tag(name='pi')
def person_info():
    return '我想测试一下'

def person_infos(*args):
    return '我想测试一下是否是列表' + '-'.join(args)

def person_infoss(*args, **kwargs):
    print('-'.join(args))
    return '我叫：' + kwargs['name'] + '-年龄：' + kwargs['age'] + '-性别：' + kwargs['sex']

register.simple_tag(func=person_infos, name="pis")
register.simple_tag(func=person_infoss, name="piss")

# list = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]
# 包标签   包含了另外一个模板的标签
@register.inclusion_tag('inclusion_tag.html', name='tab')
def get_table():
    lists = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    return {'lists': lists}


@register.inclusion_tag('inclusion_tag.html', name='tabs')
def get_tables(row, column):
    lists = []
    while row >0:
        new_list = [x for x in range(1, column + 1)]
        lists.append(new_list)
        row -= 1

    return {'lists': lists}