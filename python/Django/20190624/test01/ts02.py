import os
import sys


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test01.settings')
    import django
    django.setup()

    from app02.models import *

    # article = Articles.objects.create(title='长朋长朋长朋长朋长朋长朋')
    # print(article)
    # article = Articles.objects.get(id=1)
    # print(article)
    # 反向获取文章详情   1对1关系
    # print(article.articles_content, article.articles_content.content)

    # 正向获取文章详情
    # articles_content_obj = Articles_Content.objects.get(article_id=article.id)
    # print(articles_content_obj)
    # articles_content_obj = Articles_Content.objects.get(article=article)
    # print(articles_content_obj)

    # 根据文章附加表的conent字段找到 内容包含 长朋的数据，再查文章基础表，
    # article = Articles.objects.get(articles_content__content__contains='长朋')
    #
    # print(article)

    # 添加数据

    # conglin = Articles.objects.create(title='淙琳淙琳淙琳淙琳淙琳淙琳')
    # Articles_Content.objects.create(article=conglin, content='淙琳的自我成长！')

    # 如果基本表数据存在 而附加表数据不存在
    # 获取文章基本模型对象
    # 第一种
    # changpeng = Articles.objects.get(id=2)
    # Articles_Content.objects.create(article=changpeng, content='长朋听课很认真! ')
    # # 第二种
    # Articles_Content.objects.create(article_id=2, content='长朋听课很认真! ')

    # 删除

    # 删除基本表数据 附加表信息也会被删除
    # article = Articles.objects.get(title__contains='长朋').delete()
    # 删除附加表信息，基本表信息不会受影响
    # Articles_Content.objects.get(content__contains='长朋').delete()

    # 修改
    abc = Articles.objects.get(title='abc')
    # 修改附加表数据
    Articles_Content.objects.filter(content__contains='淙琳').update(article=abc, content='淙琳很帅，很努力！')

    # 清空一个表
    Articles.objects.all().delete()