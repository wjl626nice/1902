from django.shortcuts import render, HttpResponse

# Create your views here.

def abc(request):
    return HttpResponse('abc')

def news_show(request, id, year= None, month = None):
    return HttpResponse('aaa' + str(year) + str(id))


def news_shows(request, year=None, idstr=None):
    # 获取id
    id = idstr.split('_')[1]
    # print(idstr, type(id))

    from django.db import connection
    with connection.cursor() as cursor:
        # print(type(cursor))
        cursor.execute('select * from app01_news where id = ' + id)
        news = dictfetchall(cursor)
        # print(cursor.fetchall())
        # cursor.fetchall()
        # print(news)
        news = news[0]
    return render(request, 'news_show.html', {"news": news})


def dictfetchall(cursor):
    """
    把从数据库获取的数据 处理成字典类型
    :param cursor:
    :return:
    """
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def test(request, aaaa):
    return HttpResponse(aaaa)