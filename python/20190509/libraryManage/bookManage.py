# menu4 = (("添加书籍", 0), ("查询书籍", 1), ("下架书籍", 1))
import pymysql


# 添加书籍 需要传递 用户id
def addBook(uid):
    while True:
        bn = input("请输入新增书籍名称:")
        bp = input("请输入新增书籍价格:")
        bt = input("请输入新增书籍总数:")

        # 判断书名，书价，书数量是否符合要求
        if len(bn.strip()) != 0 and len(bp.strip()) != 0 and len(bt.strip()) != 0:
            dbconnect = pymysql.connect("192.168.9.191", "Leo", "123456789", "Library")

            # 使用cursor()方法获取操作游标
            cursor = dbconnect.cursor()
            sqlstr = "insert into book (b_name, b_price, b_total, b_reste, u_id) values ('{}','{}',{},{},{})".format(bn,
                                                                                                                     bp,
                                                                                                                     int(
                                                                                                                         bt),
                                                                                                                     int(
                                                                                                                         bt),
                                                                                                                     uid)
            # print(sqlstr)

            row = 0
            try:
                row = cursor.execute(sqlstr)
                dbconnect.commit()
            except (pymysql.Error,):
                dbconnect.rollback()
            finally:
                cursor.close()
                dbconnect.close()

            if row > 0:
                print("书籍添加成功")
                break
            else:
                print("书籍添加失败")
                break
        else:
            print("你输入书籍信息有误，请重新更改")
            break


# 查询书籍
def queryBook():
    while True:
        bn = input("请输入想要书籍名称:")

        # 判断书名是否符合要求
        if len(bn.strip()) != 0:
            dbconnect = pymysql.connect("192.168.9.191", "Leo", "123456789", "Library")

            # 使用cursor()方法获取操作游标
            cursor = dbconnect.cursor()
            sqlstr = "select * from book where b_name like '%{}%'".format(bn)
            print(sqlstr)

            books = None
            try:
                cursor.execute(sqlstr)
                books = cursor.fetchall()
            except (pymysql.Error,):
                dbconnect.rollback()
            finally:
                cursor.close()
                dbconnect.close()

            if books:
                # print(books)
                # 过滤下架书籍函数
                def xiajia(o):
                    return o[5] == 1

                # 过滤上架书籍函数
                def shangjia(o):
                    return o[5] == 0

                sjBooks = filter(shangjia, books)
                xjBooks = filter(xiajia, books)
                print("上架的书籍有：")
                for b in tuple(sjBooks):
                    print(b)

                print("下架的书籍有：")
                for b in tuple(xjBooks):
                    print(b)

                break
            else:
                print("没有找到相关书籍")
                break
        else:
            print("你输入书籍名称有误，请重新更改")
            break


# 删除书籍
def deleteBook():
    while True:
        bn = input("请输入删除书籍名称:")

        # 判断书名是否符合要求
        if len(bn.strip()) != 0:
            dbconnect = pymysql.connect("192.168.9.191", "Leo", "123456789", "Library")

            # 使用cursor()方法获取操作游标
            cursor = dbconnect.cursor()
            sqlstr = "update book set b_status = 1 where b_name = '{}'".format(bn)
            # print(sqlstr)

            row = 0
            try:
                row = cursor.execute(sqlstr)
                dbconnect.commit()
            except (pymysql.Error,):
                dbconnect.rollback()
            finally:
                cursor.close()
                dbconnect.close()

            if row > 0:
                print("书籍下架成功")
                break
            else:
                print("书籍下架失败")
                break
        else:
            print("你输入书籍名称有误，请重新更改")
            break
