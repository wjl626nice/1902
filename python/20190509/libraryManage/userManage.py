import hashlib
from sendEmail import sendCheckCodeFromEmail
import pymysql


# 注册
def register():
    print("注册")
    while True:
        un = input("请输入昵称:")
        pwd = input("请输入密码:")
        em = input("请输入邮箱地址:")

        # 判断昵称和密码，邮箱是否符合要求
        if len(un.strip()) != 0 and len(pwd.strip()) != 0 and len(em.strip()) != 0:
            break

    # 判断邮箱是否使用过
    dbconnect = pymysql.connect("192.168.9.191", "Leo", "123456789", "Library")
    # 使用cursor()方法获取操作游标
    cursor = dbconnect.cursor()

    sqlstr = "select * from user_info"
    print(sqlstr)

    try:
        cursor.execute(sqlstr)
        users = cursor.fetchall()
    except (pymysql.Error,):
        print("pymysql Error:%s".format(e))
    finally:
        cursor.close()
        dbconnect.close()

    # print(users)
    # 邮箱地址不存在
    emIsExist = False
    for u in users:
        # print(u)
        if u[5] == em:
            emIsExist = True
            break

    # 邮箱地址不存在，把昵称和密码，邮箱地址存储到 user_info 表中 ，注册成功
    if not emIsExist:
        pwd_md5 = hashlib.md5(pwd.encode('utf-8')).hexdigest()

        dbconnect2 = pymysql.connect("192.168.9.191", "Leo", "123456789", "Library")

        # 使用cursor()方法获取操作游标
        cursor2 = dbconnect2.cursor()

        sqlstr = "insert into user_info (u_name, u_pwd, u_email) values ('{}','{}','{}')".format(un, pwd_md5, em)

        rows = 0
        try:
            rows = cursor2.execute(sqlstr)
            # 提交修改
            dbconnect2.commit()
            # print(rows)
        except (pymysql.Error,):

            dbconnect2.rollback()
        finally:
            cursor2.close()
            dbconnect2.close()

        if rows > 0:
            print("注册成功")
        else:
            print("注册失败")
    else:
        # 昵称存在，那么提示用户名已存在，注册失败
        print("邮箱地址已注册，请更换邮箱地址")


# 找回密码
def findPwd():
    print("找回密码")
    while True:
        un = input("请输入你的用户名:")
        em = input("请输入你的邮箱地址:")
        # 判断邮箱地址是否符合要求
        if len(un.strip()) != 0 and len(em.strip()) != 0:

            dbconnect = pymysql.connect("192.168.9.191", "Leo", "123456789", "Library")

            # 使用cursor()方法获取操作游标
            cursor = dbconnect.cursor()
            sqlstr = "select * from user_info where u_name = '{}' and u_email = '{}'".format(un, em)
            # print(sqlstr)

            user = None
            try:
                cursor.execute(sqlstr)
                user = cursor.fetchone()
            except (pymysql.Error,):
                dbconnect.rollback()
            finally:
                cursor.close()
                dbconnect.close()

            if user:
                break

    # 发送验证码
    randomcc = sendCheckCodeFromEmail(em)
    # print(randomcc)

    inputcc = input("请输入正确的验证码:")

    if inputcc == randomcc:
        inputpwd = input("请输入新的密码:")

        pwd_md5 = hashlib.md5(inputpwd.encode('utf-8')).hexdigest()

        dbconnect = pymysql.connect("192.168.9.191", "Leo", "123456789", "Library")

        # 使用cursor()方法获取操作游标
        cursor = dbconnect.cursor()
        sqlstr = "update user_info set u_pwd = '{}' where u_email = '{}'".format(pwd_md5, em)
        # print(sqlstr)

        rows = 0
        try:
            rows = cursor.execute(sqlstr)
            # 提交修改
            dbconnect.commit()
            # print(rows)
        except (pymysql.Error,):
            dbconnect.rollback()
        finally:
            cursor.close()
            dbconnect.close()

        if rows > 0:
            print("密码重置成功")
        else:
            print("密码重置失败")
    else:
        print("你输入的验证码有误")



# 0为普通会员，1为超级管理员，2为普通管理员
privileges = (("普通会员", 0), ("超级管理员", 1), ("普通管理员", 2))


def login():
    while True:
        em = input("请输入邮箱地址:")
        pwd = input("请输入密码:")

        # 判断密码，邮箱是否符合要求
        if len(pwd.strip()) != 0 and len(em.strip()) != 0:
            pwd_md5 = hashlib.md5(pwd.encode('utf-8')).hexdigest()
            dbconnect = pymysql.connect("192.168.9.191", "Leo", "123456789", "Library")

            # 使用cursor()方法获取操作游标
            cursor = dbconnect.cursor()
            sqlstr = "select * from user_info where u_email = '{}' and u_enabled = 1 and u_pwd = '{}'".format(em,
                                                                                                              pwd_md5)
            # print(sqlstr)

            user = None
            try:
                cursor.execute(sqlstr)
                user = cursor.fetchone()
            except (pymysql.Error,):
                dbconnect.rollback()
            finally:
                cursor.close()
                dbconnect.close()

            if user:
                # print(user)
                # print("'{}','{}'登录成功".format(privileges[user[3]][0], user[1]))
                return user
            else:
                print("登录失败")
                return tuple()
        else:
            print("你输入邮箱地址或者密码有误，请重新登录")
            return tuple()


# 授权用户权限
def shouquan():
    print("\n会员权限如下：")
    for x in privileges:
        print("{}:{}".format(x[0], x[1]))

    while True:
        em = input("请输入邮箱地址:")
        pri = input("请输入对应的权限:")

        # 判断密码，邮箱是否符合要求
        if len(em.strip()) != 0 and int(pri) in range(0, 3):
            dbconnect = pymysql.connect("192.168.9.191", "Leo", "123456789", "Library")

            # 使用cursor()方法获取操作游标
            cursor = dbconnect.cursor()
            sqlstr = "update user_info set u_pri = {}  where u_email = '{}'".format(pri, em)
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
                print("权限修改成功")
                break
            else:
                print("权限修改失败")
                break
        else:
            print("你输入邮箱地址或者权限有误，请重新更改")
            break


# 会员状态：1表示用户可用，0表示禁用用户
status = (("禁用用户", 0), ("用户可用", 1))


# 更改用户状态
def changeUserStatus():
    print("\n用户状态如下：")
    for x in status:
        print("{}:{}".format(x[0], x[1]))

    while True:
        em = input("请输入邮箱地址:")
        st = input("请输入对应的状态:")

        # 判断密码，邮箱是否符合要求
        if len(em.strip()) != 0 and int(st) in range(0, 2):
            dbconnect = pymysql.connect("192.168.9.191", "Leo", "123456789", "Library")

            # 使用cursor()方法获取操作游标
            cursor = dbconnect.cursor()
            sqlstr = "update user_info set u_enabled = {}  where u_email = '{}'".format(st, em)
            # print(sqlstr)

            try:
                row = cursor.execute(sqlstr)
                dbconnect.commit()
            except (pymysql.Error,):
                dbconnect.rollback()
            finally:
                cursor.close()
                dbconnect.close()

            if row > 0:
                print("状态修改成功")
                break
            else:
                print("状态修改失败")
                break
        else:
            print("你输入邮箱地址或者状态有误，请重新更改")
            break
