# menu4 = (("添加书籍", 0), ("查询书籍", 1), ("下架书籍", 1))


def addBook():
    while True:
        bn = input("请输入新增书籍名称:")
        bp = input("请输入新增书籍价格:")
        bt = input("请输入新增书籍总数:")

        # 判断密码，邮箱是否符合要求
        if len(bn.strip()) != 0 and len(bp.strip()) != 0 and len(bt.strip()) != 0:
            dbconnect = pymysql.connect("192.168.9.191", "Leo", "123456789", "Library")

            # 使用cursor()方法获取操作游标
            cursor = dbconnect.cursor()
            sqlstr = "insert into book (b_name, b_price, b_total) values ('{}','{}',{})".format(bn, bp, int(bp))
            print(sqlstr)

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


def queryBook():
    print("查询书籍")


def deleteBook():
    print("下架书籍")
