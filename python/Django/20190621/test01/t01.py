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
    # ret = Press.objects.exclude(id__lt=2)
    # print(ret)

    # 2019-6-21 上边是20号测试代码，下边21号

    """
    start
    字段类型 字段参数 简单增删改查操作
    """
    # 向书表添加数据
    # Books.objects.create(books_name='三国演义', press_id=10)
    # 向作者表添加数据
    # Author.objects.create(name='邓帅', email='adfad233')

    # 测试关联关系字段
    # book = Books.objects.get(id=1)
    # print(book.press)

    press = Press.objects.get(id=10)
    # 反向获取模型数据
    # print(press.id)
    # books = Books.objects.filter(press_id=press.id)
    # print(books)
    # books = press.books_set.all()
    # print(books)
    books = press.pb.all()
    print(books)

    # 获取出版社，测试排序
    presss = Press.objects.all()
    print(presss)

    """
    end
    """
    print('*'*50)
    """继续20号查询相关的代码"""
    # 查询出版社除了宋瑜出版社之外的其他
    press = Press.objects.exclude(press_name='宋瑜出版社')
    print(press)
    press = Press.objects.exclude(id__lt=13)
    print(press)

    print('方法：values'.center(80, '*'))
    # 返回指定字段的结果，不会获取所有字段，values查询的结果给了QuerySet集合
    books = Books.objects.values('books_name', 'publish_date')
    print(books)

    print('方法：values_list'.center(80, '*'))
    books = Books.objects.values_list('books_name', 'publish_date')
    print(books)

    print('在Meta中设置默认排序：ordering'.center(80, '*'))
    books = Books.objects.values_list('books_name', 'publish_date')
    print(books)

    print('方法：order_by'.center(80, '*'))
    # books = Books.objects.values_list('books_name', 'publish_date').order_by('-id')

    print('方法：reverse反转'.center(80, '*'))
    books = Books.objects.values_list('books_name', 'publish_date').order_by('-id').reverse()   # reverse 反转排序，但是必须是数据已经被排序
    print(books)

    print('方法：count'.center(80, '*'))
    # count = Books.objects.count()
    count = Books.objects.all().count()
    print(count)

    print('方法：first'.center(80, '*'))
    # book = Books.objects.first()

    print('方法：last'.center(80, '*'))
    book = Books.objects.last()    # 获取最后一条
    book = Books.objects.reverse().first()  # 反转后获取第一条（最后一条）
    print(book)

    print('方法：exists'.center(80, '*'))
    # ret = Books.objects.exists()
    ret = Books.objects.filter(id__gt=15).exists()
    print(ret)

    print('单表双下划线查询'.center(80, '*'))
    # ret = Books.objects.filter(publish_date__year=2018)
    ret = Books.objects.filter(publish_date__day=10)
    print(ret)

    print('外键的跨表查询'.center(80, '*'))
    book = Books.objects.get(id=8)
    book_press_obj = book.press   # 根据书对象获取出版社对象
    print(book, book_press_obj, book_press_obj.press_name, type(book_press_obj))

    # 基于双下划线，跨表查询。
    ret = Books.objects.filter(id=8).values('books_name', 'press__press_name')
    print(ret)



