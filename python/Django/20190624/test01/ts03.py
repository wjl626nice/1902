import os
import sys


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test01.settings')
    import django
    django.setup()

    # 第一种方式通过多对多 关联关系器操作
    from app01 import models as apm
    # 指定作者的所有书
    dengshuai_of_all_books = apm.Author.objects.get(id=5).bookss.all()
    print(dengshuai_of_all_books)

    # 第二种 通过多对多关系 自建关联表，通过ForeignKey实现关系查询
    from app03 import models as apm3
    # 指定作者的所有书
    # 获取邓帅写的所有书的id
    dengshuai_of_books_id = apm3.Author2Books.objects.filter(author_id=5).values('books_id')
    print(dengshuai_of_books_id)
    # 列表生成式
    books_ids = [books_id['books_id'] for books_id in dengshuai_of_books_id]
    # 上下效果一样，生成一个列表
    # books_ids = []
    # for books_id in dengshuai_of_books_id:
    #     books_ids.append(books_id['books_id'])

    books = apm3.Books.objects.filter(id__in=books_ids)  # [1,3,6] (1,3,6)
    print(books)

    # 第三种 方式
    from app04 import models as apm4

    # 指定作者的所有书
    ret = apm4.Books.objects.filter(author__id=5)
    print(ret,type(ret))