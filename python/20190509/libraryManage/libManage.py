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
    # 用户名不存在
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

        # sqlstr = "insert into user_info (u_name, u_pwd, u_email) values ('wjl','112211','wangjl626@live.com')"
        print(sqlstr)

        try:
            rows = cursor2.execute(sqlstr)
            # 提交修改
            dbconnect2.commit()
            print(rows)
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
            print(sqlstr)

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
        print(sqlstr)

        try:
            rows = cursor.execute(sqlstr)
            # 提交修改
            dbconnect.commit()
            print(rows)
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


# 退出系统
def logout():
    print("注销登录")

    # assert 断言，停止程序执行
    assert False


menu = (("会员注册", 0), ("会员登录", 1),("密码找回", 2), ("退出系统", 3))

while True:
    for x in menu:
        print("{}:{}".format(x[0], x[1]))

    index = int(input("请选择功能:"))

    if index == 0:
        register()
    elif index == 1:
        login()
    elif index == 2:
        findPwd()
    elif index == 3:
        logout()
