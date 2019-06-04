from django.shortcuts import render, HttpResponse, redirect
#  导入app的模型
from manager.models import *
# from manager import models

# Create your views here.
def press_list(request):
    """
    出版社列表
    :param request:
    :return:
    """
    # 接收http传递的参数
    kw = request.GET.get('kw', None)
    # 从数据表（manager_press）中获取所有的数据，并且对数据进行倒序
    # print(kw)
    if kw:
        # filter 过滤获取
        presss = Press.objects.filter(press_name=kw).order_by('-id')  # press.objectspresss = press.objects.filter(press_name=kw).order_by('-id')  # press.objects.all() ===  select  * from manager_press
    else:
        # 直接获取所有数据
        presss = Press.objects.all().order_by('-id')  # press.objectspresss = press.objects.filter(press_name=kw).order_by('-id')  # press.objects.all() ===  select  * from manager_press
    # print(presss)

    # with open('press_list.html', 'r+') as f:
    #     content = f.read()
    #
    # return HttpResponse(content)

    return render(request, 'press_list.html', {'presss': presss})

def press_add(request):
    """
    添加出版社
    :param request:
    :return:
    """
    error_msg = ''
    if request.method == 'POST':
        # 获取form提交的参数
        press_name = request.POST.get('press_name', None).strip()
        print(press_name, type(press_name))
        # press_name 只有有值 就是True,空就是 Flase: ""、''、Flase、None、0
        if press_name:
            # 添加出版社
            Press.objects.create(press_name=press_name)
            # 跳转到出版社管理列表
            return redirect('/press_list')
        else:
            error_msg = '请输入出版社名字！'

    return render(request, 'press_add.html', {'error_msg': error_msg})


def press_del(request):
    """
    出版社删除
    :param request:
    :return:
    """
    id = request.GET.get('id')
    if id:
        try:
            # 查询到指定id数据然后删除
            Press.objects.get(id=id).delete()
        # except NameError as e:
        #     print(e)
        except Exception as e:
            print(e)
            return HttpResponse('数据不存在！')

    else:
        return HttpResponse('要删除的出版社不存在！')
    return redirect('/press_list')

def press_edit(request):
    """
    展示修改页面和保存修改信息
    :param request:
    :return:
    """
    id = request.GET.get('id')
    error_msg = ''
    if request.method == 'POST':
        # 新的出版社名字
        name = request.POST.get('press_name')
        if name:
            #  根据出版社id查询出出版社
            # press_obj = objcet{"id":1,'press_name': '北京出版社'}
            press_obj = Press.objects.get(id=id)   # select * from manager_press where id = 1
            press_obj.press_name = name
            # press_obj = objcet{"id":1,'press_name': '新的出版社名字'}
            # 更新对象本身
            try:
                press_obj.save()
            except Exception as e:
                # print(e, type(e), e.args, type(e.args))
                # 1062错误代表 "Duplicate entry '牛超出版社' for key 'press_name'"
                if e.args[0] == 1062:
                    return HttpResponse('<script>alert("该出版社已存在");location.href="/press_list"</script>')
            # save 先判断press_obj对象是否有一个id,并且不为空就拼接update 语句：
            # update manager_press set press_name= '新的出版社名字' where id = 1
            # 如果id为空会拼接insert语句 insert into manager_press(id,press_name)
            # values(null,'新的出版社名')。然后把语句发送给DBMS（数据库管理系统）执行
            return redirect('/press_list')
        else:
            error_msg = '请输入用户名！'

    # 获取要修改的出版社信息
    press_obj = Press.objects.get(id=id)
    return render(request, 'press_edit.html', {'press': press_obj, 'error_msg': error_msg})

def book_list(request):
    """
    书列表
    :param request:
    :return:
    """
    # 接收http传递的参数
    kw = request.GET.get('kw', None)
    # 从数据表（manager_press）中获取所有的数据，并且对数据进行倒序
    # print(kw)
    if kw:
        # filter 过滤获取
        book_objs = Books.objects.filter(press_name=kw).order_by('-id')  # books.objectsbooks = books.objects.filter(books_name=kw).order_by('-id')  # books.objects.all() ===  select  * from manager_books
    else:
        # 直接获取所有数据
        book_objs = Books.objects.all().order_by('-id')  # books.objectsbooks = books.objects.filter(books_name=kw).order_by('-id')  # books.objects.all() ===  select  * from manager_books
    # print(presss)

    # with open('press_list.html', 'r+') as f:
    #     content = f.read()
    #
    # return HttpResponse(content)

    return render(request, 'books_list.html', {'books': book_objs})


def book_add(request):
    """
    添加图书
    :param request:
    :return:
    """
    error_msg = ''
    if request.method == 'POST':
        # 获取form提交的参数
        book_name = request.POST.get('book_name', None).strip()
        # 获取出版社id
        press_id = request.POST.get('press')
        print(book_name, type(book_name))
        # book_name 只有有值 就是True,空就是 Flase: ""、''、Flase、None、0
        if book_name:

            # 添加图书  第一种方式
            Books.objects.create(books_name=book_name, press_id=press_id)

            # 添加图书  第二种方式
            # 获取出版社对象
            # press_obj = Press.objects.get(id=press_id)
            # Books.objects.create(books_name=book_name, press=press_obj)

            # 跳转到图书管理列表
            return redirect('/book_list')
        else:
            error_msg = '请输入图书名字！'

    # 获取所有的出版社
    press_objs = Press.objects.all().order_by('-id')
    return render(request, 'book_add.html', {'error_msg': error_msg, 'presss': press_objs})

def book_del(request):
    """
    书删除
    :param request:
    :return:
    """
    id = request.GET.get('id')
    if id:
        try:
            # 查询到指定id数据然后删除
            Books.objects.get(id=id).delete()
        # except NameError as e:
        #     print(e)
        except Exception as e:
            print(e)
            return HttpResponse('数据不存在！')

    else:
        return HttpResponse('要删除的书不存在！')
    return redirect('/book_list')

def book_edit(request):
    """
    展示修改页面和保存修改信息
    :param request:
    :return:
    """
    error_msg = ''
    if request.method == 'POST':
        # 获取要修改的书的id
        id = request.POST.get('id')
        # 新的书名字
        name = request.POST.get('book_name')
        #  获取出版社id
        press_id = request.POST.get('press')
        if name:
            #  根据书id查询出书
            book_obj = Books.objects.get(id=id)
            book_obj.books_name = name
            # 通过数据库的字段修改表数据
            book_obj.press_id = press_id
            # 通过模型的 关联字段修改表数据
            # book_obj.press = Press.objects.get(id=press_id)

            # 更新对象本身
            try:
                book_obj.save()
            except Exception as e:

                if e.args[0] == 1062:
                    return HttpResponse('<script>alert("该书已存在");location.href="/book_list"</script>')
            return redirect('/book_list')
        else:
            error_msg = '请输入书名！'

    id = request.GET.get('id')
    # 获取要修改的书信息
    book_obj = Books.objects.get(id=id)
    # 获取所有出版社
    presss = Press.objects.all().order_by('-id')
    return render(request, 'book_edit.html', {'book': book_obj, 'presss': presss, 'error_msg': error_msg})

def author_list(request):
    """
    作者管理
    :param request:
    :return:
    """
    # 获取所有的作者
    authors = Author.objects.all().order_by('-id')
    print(authors)
    return render(request, 'author_list.html', {"authors": authors})

def author_add(request):
    if request.method == 'POST':
        # 获取作者名字
        author_name = request.POST.get('author_name')

        # 获取作品的id
        book_id = request.POST.get('book')

        # 获取书的对象
        # book = Books.objects.getlist(id=book_id)

        # 获取选择书的id
        booklist = request.POST.getlist('book')  # ['3','4'] 书的id

        # 向作者表添加作者
        author_obj = Author.objects.create(name=author_name)
        # 通过关联关系器 bookss  让 作者对象和书对象建立关联
        author_obj.bookss.set(booklist)  # booklist 可以有两种类型的值：对象列表  id列表
        # 添加成功以后返回到列表
        return  redirect('/author_list')
    # 获取所有书
    book_objs = Books.objects.all().order_by('-id')
    return render(request, 'author_add.html', {"books": book_objs})

def author_del(request):
    """
    删除作者
    :param request:
    :return:
    """
    id = request.GET.get('id')
    if id:
        # 删除作者
        Author.objects.get(id=id).delete()
        return redirect('/author_list')
    else:
        return HttpResponse('要删除的作者不存在！')

def author_edit(request):
    if request.method == 'POST':
        # 获取要修改的作者id
        id = request.POST.get('id')
        # 获取作者的名字
        new_name = request.POST.get('author_name')
        # 获取作品idlist
        idlist = request.POST.getlist('book')
        # 获取作者对象
        author = Author.objects.get(id=id)
        # 改变旧的名字
        author.name = new_name
        # 执行当前作者的更新操作
        author.save()
        # 更新当前作者的对应的作品
        author.bookss.set(idlist)
        # 跳转到作者列表
        return redirect('/author_list')

    id = request.GET.get('id')
    # 根据id获取作者信息
    author = Author.objects.get(id=id)
    # 获取所有书
    book_objs = Books.objects.all().order_by('-id')
    # print(book_objs)
    # for book in book_objs:
    #     print(book,book.books_name)
    return render(request, 'author_edit.html', {'books': book_objs, 'author': author})