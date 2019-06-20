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

    from app02.models import *

    # 可以对模型进行操作

    # 添加数据
    # Press.objects.create(press_name='清华出版设')
    # Press.objects.create(press_name='北京出版设')
    # Press.objects.create(press_name='宋瑜出版设')
    # Press.objects.create(press_name='浙大出版设')

    # 查询数据    all会把查询到的数据放入到QurySet集合中
    # ret = Press.objects.all()
    # print(ret)

    # 查询宋瑜出版社   get查询单个对象
    # ret = Press.objects.get(press_name='宋瑜出版社')
    # print(ret)

    # 查询清华出版社   get查询不存在数据时会报错
    # ret = Press.objects.get(press_name='清华1出版社')
    # print(ret)

    # 查询大地出版社 filter查询结果集放入到QuerySet集合中，不存在时返回一个空QuerySet集合
    # dd = Press.objects.filter(press_name='大地出版社')
    # print(dd)
    # yusong = Press.objects.filter(press_name='宋瑜出版社')
    # print(yusong)

    # 查询id>2的数据
    ret = Press.objects.exclude(id__lt=2)
    print(ret)
