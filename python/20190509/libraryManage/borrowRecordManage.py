import pymysql


# 借书 需要传递 用户id
def borrowBook(uid):
    while True:
        bn = input("请输入你要借的书籍名称:")

        # 判断书名是否符合要求
        if len(bn.strip()) != 0:
            dbconnect = pymysql.connect("192.168.9.191", "Leo", "123456789", "Library")

            # 使用cursor()方法获取操作游标
            cursor = dbconnect.cursor()
            sqlstr1 = "select * from book where b_name = '{}' and b_status = 0".format(bn)
            cursor.execute(sqlstr1)
            book = cursor.fetchone()

            if book and book[4] > 0:

                # 根据用户id 和 书籍 id ,查询是否有借阅记录
                sqlstr11 = "select * from borrow_record where u_id = {} and b_id = {}".format(uid, book[0])
                cursor.execute(sqlstr11)
                record = cursor.fetchone()

                if record is None:
                    sqlstr2 = "update book set b_reste = {} where b_name = '{}'".format(book[4] - 1, bn)
                    sqlstr3 = "insert into borrow_record (u_id, b_id)  values ({}, {})".format(uid, book[0])
                    print(sqlstr2)
                    print(sqlstr3)

                    try:
                        cursor.execute(sqlstr2)
                        cursor.execute(sqlstr3)
                        dbconnect.commit()
                        print("借书成功")
                    except (pymysql.Error,):
                        dbconnect.rollback()
                        print("借书失败")
                    finally:
                        cursor.close()
                        dbconnect.close()

                    # 跳出while循环
                    break
                else:
                    print("你已经借阅过这本书")
                    break
            else:
                print("书不存在或者书被借完，借书失败")
                cursor.close()
                dbconnect.close()
                break
        else:
            print("你输入书籍名称有误，请重新更改")
            break


# 还书 需要传递 用户id
def giveBackBook(uid):
    while True:
        bn = input("请输入你要还的书籍名称:")

        # 判断书名是否符合要求
        if len(bn.strip()) != 0:
            dbconnect = pymysql.connect("192.168.9.191", "Leo", "123456789", "Library")

            # 使用cursor()方法获取操作游标
            cursor = dbconnect.cursor()

            # 根据书名查询 书的信息
            sqlstr1 = "select * from book where b_name = '{}'".format(bn)
            cursor.execute(sqlstr1)
            book = cursor.fetchone()
            if book:
                # 根据用户id 和 书籍 id ,查询是否有借阅记录
                sqlstr11 = "select * from borrow_record where u_id = {} and b_id = {}".format(uid, book[0])
                cursor.execute(sqlstr11)
                record = cursor.fetchone()

                if record:
                    sqlstr2 = "update book set b_reste = {} where b_name = '{}'".format(book[4]+1, bn)
                    sqlstr3 = "delete from borrow_record where u_id = {} and b_id = {}".format(uid, book[0])
                    print(book)
                    print(sqlstr2)
                    print(sqlstr3)

                    try:
                        cursor.execute(sqlstr2)
                        cursor.execute(sqlstr3)
                        dbconnect.commit()
                        print("还书成功")
                    except (pymysql.Error,):
                        dbconnect.rollback()
                        print("还书失败")
                    finally:
                        cursor.close()
                        dbconnect.close()

                    # 跳出while循环
                    break
                else:
                    print("借书记录不存在")
                    cursor.close()
                    dbconnect.close()
                    break
            else:
                print("书不存在")
                break
        else:
            print("你输入书籍名称有误，请重新更改")
            break
