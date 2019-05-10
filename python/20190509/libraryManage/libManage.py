from userManage import *
from bookManage import *

menu1 = (("会员注册", 0), ("会员登录", 1), ("密码找回", 2), ("退出系统", 3))
menu2 = (("借阅书籍", 0), ("归还书籍", 1))
menu3 = (("会员授权", 0), ("更改用户状态", 1))
menu4 = (("添加书籍", 0), ("查询书籍", 1), ("下架书籍", 2))

loginedUser = tuple()

while True:
    menu = menu1
    # loginedUser[3] 表示用户权限  0为普通会员，1为超级管理员，2为普通管理员
    print(loginedUser)
    if len(loginedUser) == 6:
        if loginedUser[3] == 0:
            menu = menu2
        elif loginedUser[3] == 1:
            menu = menu3
        elif loginedUser[3] == 2:
            menu = menu4


    print("\n")
    for x in menu:
        print("{}:{}".format(x[0], x[1]))

    str = input("请选择功能:")

    # 判断输入的是否是数字，如果输入的不是数字，请重新输入，如果不做这个判断，直接转成整数的时候，会报错
    if not str.isdigit():
        continue
    index = int(str)

    if len(loginedUser) == 0:
        if index == 0:
            register()
        elif index == 1:
            loginedUser = login()
        elif index == 2:
            findPwd()
        elif index == 3:
            logout()
    elif len(loginedUser) == 6:
        if loginedUser[3] == 0:
            pass
        elif loginedUser[3] == 1:
            if index == 0:
                shouquan()
            elif index == 1:
                changeUserStatus()
        elif loginedUser[3] == 2:
            if index == 0:
                pass
                # addBook()
            elif index == 1:
                pass
                # queryBook()
            elif index == 2:
                pass
                # deleteBook()
