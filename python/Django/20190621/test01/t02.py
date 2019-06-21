import os
import sys

if __name__ == '__main__':
    # 设置django启动时的配置文件
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test01.settings')
    # 导入django项目
    import django
    # print(django.get_version())
    # 启动django
    django.setup()

    from app03.models import *

    # 向文章表添加数据
    # article = Articles.objects.create(title='测试测试测试测试测试测试测试测试测试测试')
    article = Articles.objects.get(id=4)
    print(article.Articles_Content)
    # Articles_Content.objects.create(article=article, content='测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试测试')
