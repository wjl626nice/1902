import os
import sys


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test01.settings')
    import django
    django.setup()

    from app01.models import *

    # 查询测试

    press = Press.objects.all()
    # print(press)
    # # press = Press.objects.values('press_name')
    # press = Press.objects.values_list('press_name')
    # print(press)
    # press = Press.objects.filter(press_name='人民出版社11').exists()
    # print(press)
    # # press_name__contains   press_name__icontains:忽略大小写 一般字母查询
    # press = Press.objects.filter(press_name__contains='出版社').count()
    # print(press)

    print('单表的双下划线查询'.center(80, '*'))
    # 单表的双下划线查询

    # press = Press.objects.filter(id__gt=2)   # 查询id大于2
    # print(press)
    #
    # # 查询销量大于等于10小于等于30的书
    # books = Books.objects.filter(sales_num__gte=10, sales_num__lte=30)
    # print(books)
    # # 查询id 是2，3，4的出版社
    # press = Press.objects.filter(id__in=(2, 3, 4)).values('press_name')
    # print(press)
    # # 查询以山字 开始的所有书
    # books = Books.objects.filter(books_name__startswith='山')
    # print(books)
    # # 查询2016出的所有书       publish_date` BETWEEN '2016-01-01' AND '2016-12-31'
    # books = Books.objects.filter(publish_date__year=2016).values('id', 'books_name')
    # print(books)
    #
    # print('外键的跨表查询'.center(80, '*'))
    # books = Books.objects.filter(id=1).values('books_name', 'press__press_name')
    # print(books)

    # 基于对象的反向查询
    # press_obj = Press.objects.get(id=4)
    # # get_books_by_press = press_obj.books_set.all()
    # get_books_by_press = press_obj.pb.all()
    # print(get_books_by_press)
    #
    # # Press.objects.filter(id=5).values('press_name', 'books__books_name')
    # Press.objects.filter(id=5).values('press_name', 'pb__books_name')

    print('ManyToManyField: 多对多'.center(80, '*'))

    # 查询一个作者
    # author_obj = Author.objects.last()
    # print(author_obj.name)
    # author_of_books = author_obj.bookss.all()   # bookss关联关系管理器
    # print(author_of_books)

    # 1、create
    # 通过作者添加一本书
    # 先添加一本书，获取id，然后再把书的id和作者的id放入到关联表中

    # 以上需求可以通过两步完成：
    # 1、在books表中添加一本书
    # 2、在作者和书的关联表中添加关系数据


    # obj = author_obj.bookss.create(books_name='胖子的逆袭')

    # author_obj.bookss.create 执行了四条sql语句
    """
    1、根据作者的id 查询作者的所有书（author_obj.bookss）
        SELECT `app01_books`.`id`, `app01_books`.`books_name`, `app01_books`.`press_id`, `app01_books`.`publish_date`, `app01_books`.`price`, `app01_books`.`stock`, `app01_books`.`sales_num`, `app01_books`.`us_shelf` FROM `app01_books` INNER JOIN `app01_author_bookss` ON (`app01_books`.`id` = `app01_author_bookss`.`books_id`) WHERE `app01_author_bookss`.`author_id` = 2 ORDER BY `app01_books`.`id` ASC  LIMIT 21;
    2、向书表添加一本书 （bookss.create）
        INSERT INTO `app01_books` (`books_name`, `press_id`, `publish_date`, `price`, `stock`, `sales_num`, `us_shelf`) VALUES ('胖子的逆袭', 1, '2019-06-24', '0.00', 50, 0, 0);
    3、需要向关联表中添加关系，所以先检查关系表中是否已经存在了关系
        SELECT `app01_author_bookss`.`books_id` FROM `app01_author_bookss` WHERE (`app01_author_bookss`.`author_id` = 2 AND `app01_author_bookss`.`books_id` IN (5));
    4、如果没有关系，那么向关联表中添加作者和书的关系
        INSERT INTO `app01_author_bookss` (`author_id`, `books_id`) VALUES (2, 5); 
    """
    # print(obj)


    # 2、add
    # 在关联关系表中添加一条数据，邓帅写的书的记录
    # 获取作者对象
    # author_obj = Author.objects.get(id=5)

    # 获取书对象
    # books_obj = Books.objects.get(id=2)

    # 对作者添加指定的书
    # author_obj.bookss.add(books_obj)

    # 添加多个对象
    # books = Books.objects.filter(id__in=[1, 3])
    # print(books)
    # 让邓帅参与写书id是1和3
    # Author.objects.get(id=5).bookss.add(*books)  # 把列表打散传入

    # 直接给作者直接添加指定的书
    # Author.objects.get(id=6).bookss.add(2)  # 2 为书id



    # 3、remove
    # books = Books.objects.get(id=2)

    # 在邓帅写的书中删除 id=2的这本书
    # Author.objects.get(id=5).bookss.remove(books)

    # 在邓帅写的书中删除 id=1的这本书
    # Author.objects.get(id=5).bookss.remove(1)

    # 根据书删除指定的作者（反向操作）
    # Books.objects.get(id=3).author_set.remove(5)


    # clear
    # 清空
    # 把东洋写的所有书删除（关系表的关系删除）
    # Author.objects.get(id=6).bookss.clear()



    # 外键的反向操作
    # 通过反向clear操作
    # press_obj = Press.objects.get(id=1)
    # 关联关系管理器  如果外键参数中有related_name='pb': press_obj.pb, 没有的话是 press_ojb.books_set
    # clear方法，可能不存在，因为字段不允许为空。把它设置允许为空就有clear方法了
    # press_obj.pb.clear()  # 会把 books表中的关联字段设置为null



    print('聚合函数和分组查询'.center(80, '*'))

    from django.db.models import Avg, Count, Max, Min, Sum
    # 求所有书的平均价格
    # ret = Books.objects.all().aggregate(Avg('price'))
    # print(ret)
    # ret = Books.objects.all().aggregate(Max('price'))
    # print(ret)
    # ret = Books.objects.all().aggregate(minprice=Min('price'))  # 自定义字段别名
    # print(ret)

    # aggregate 合计聚合

    # ret = Books.objects.all().aggregate(maxprice=Max('price'), minprice=Min('price'), count=Count('stock'))  # 自定义字段别名
    # print(ret)
    # 取值
    # print(ret['count'], ret.get('maxprice'))

    # 查询邓帅写了几本书
    # count = Author.objects.get(id=5).bookss.all().count()
    # count = Author.objects.filter(id=5).values('id', 'name').annotate(books_num=Count('bookss'))
    # # count = Books.objects.annotate(books_num=Count('author'))
    # print(count)
    #
    # # 每个作者写了几本书
    # authors = Author.objects.values('id', 'name').annotate(books_num=Count('bookss'))
    # print(authors)
    # # 每本书的作者书
    # books = Books.objects.values('id', 'books_name').annotate(author_num=Count('author'))
    # print(books)
    # # 查询作者数大于1的书
    # books = Books.objects.values('id', 'books_name').annotate(author_num=Count('author')).filter(author_num__gt=1)
    # print(books)

    # 查询各个作者写的书的总价格（作业）

    print('F查询和Q查询'.center(80,'*'))
    books = Books.objects.filter(sales_num__gt=0)
    print(books)

    # 查询出 销量大于库存的所有书，（两个字段对比）通过F查询

    from django.db.models import F

    books = Books.objects.filter(sales_num__gt=F('stock'))
    # 两个字段对比时使用F查询
    print(books)

    # 对单本书的销量更新
    # books_obj = Books.objects.get(id=5)
    # # books_obj.sales_num = books_obj.sales_num + 10
    # books_obj.sales_num += 10
    # books_obj.save()

    # 批量更新所有书的库存
    # Books.objects.update(stock=F('stock') + 100)

    # 批量更新所有书的销量（翻两倍）
    # Books.objects.update(sales_num=F('sales_num') * 2)

    # 批量向所有书的名字后边加 第一版

    # Concat 将多个字符串拼接到一起，是mysql中重要的内置函数
    # from django.db.models.functions import Concat
    # from django.db.models import Value
    # Books.objects.update(books_name=Concat(F('books_name'), Value('第一版')))

    # Q
    from django.db.models import Q
    # 求销量 大于1000 小于 2000的所有书
    books = Books.objects.filter(sales_num__gt=1000, sales_num__lt=2000)
    print(books)

    # 求销量 小于500  或者 价格大于50的所有书
    books = Books.objects.filter(Q(sales_num__lt=500) | Q(price__gt=50))
    print(books)

    # 求销量 小于500  或者 价格大于50的  并且以大开始的所有书
    books = Books.objects.filter(Q(sales_num__lt=500) | Q(price__gt=50), books_name__startswith='大')
    print(books)