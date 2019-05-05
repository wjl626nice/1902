import hashlib


# 注册
def register():
    print("注册")
    while True:
        un = input("请输入用户名:")
        pwd = input("请输入密码:")
        # 判断用户名和密码是否符合要求
        if len(un.strip()) != 0 and len(pwd.strip()) != 0:
            break

    # 判断用户名是否存在
    f = open("./db/user_info.txt", "r")
    users = f.readlines()
    f.close()

    # 用户名不存在
    unIsExist = False
    for u in users:
        tempUn = u.split("|")[0]
        if tempUn == un:
            unIsExist = True
            break

    # 用户名不存在，把用户名和密码存储到 ./db/user_info.txt ，注册成功
    '''
    用户名|密码|权限|....
    '''
    if not unIsExist:
        pwd_md5 = hashlib.md5(pwd.encode('utf-8')).hexdigest()
        str1 = un + "|" + pwd_md5 + "|" + "1" + "|" + "1" + "\n"
        f = open("./db/user_info.txt", "a")
        f.write(str1)
        f.close()

        print("注册成功")
    else:
        # 用户名存在，那么提示用户名已存在，注册失败
        print("用户名已存在，注册失败")


# 登录
def login():
    print("登录")
    while True:
        un = input("请输入用户名:")
        pwd = input("请输入密码:")
        # 判断用户名和密码是否符合要求
        if len(un.strip()) != 0 and len(pwd.strip()) != 0:
            break

    # 下面这样操作文件，当操作完毕之后，会自动的关闭文件对象
    with open("./db/user_info.txt", "r") as f:
        users = f.readlines()

    # 判断用户名和密码是否正确
    for u in users:
        user_list = u.split("|")
        pwd_md5 = hashlib.md5(pwd.encode('utf-8')).hexdigest()
        if user_list[0] == un and user_list[1] == pwd_md5:
            if user_list[2] == "1":
                print("恭喜你，登录成功")
                global isLogin
                isLogin = True

                global usernameOfLogined
                usernameOfLogined = un
                return
            else:
                print("你的账户已经被冻结，请线下联系管理员")
                return

    print("登录失败，用户名或者密码不正确")


# 是否有用户登录
isLogin = False
# 登录用户名
usernameOfLogined = ""


# 找回密码
def findPwd():
    print("找回密码")
    while True:
        un = input("请输入用户名:")
        pwd = input("请输入密码:")
        # 判断用户名和密码是否符合要求
        if len(un.strip()) != 0 and len(pwd.strip()) != 0:
            break

    with open("./db/user_info.txt", "r") as f:
        users = f.readlines()

    # 判断用户名和密码是否正确
    newStr = ""
    for u in users:

        user_list = u.split("|")
        pwd_md5 = hashlib.md5(pwd.encode('utf-8')).hexdigest()
        if user_list[0] == un:
            newStr += un + "|" + pwd_md5 + "|" + "1" + "|" + "1" + "\n"
        else:
            newStr += u

    with open("./db/user_info.txt", "w") as f:
        f.write(newStr)


# 注销登录
def logout():
    print("注销登录")

    # assert 断言，停止程序执行
    assert False


# 冻结用户
def freezeUser():
    while True:
        un = input("请输入用户名:")
        # 判断用户名和密码是否符合要求
        if len(un.strip()) != 0:
            break

    with open("./db/user_info.txt", "r") as f:
        users = f.readlines()

    # 判断用户名和密码是否正确
    newStr = ""
    for u in users:
        user_list = u.split("|")
        if user_list[0] == un:
            newStr += un + "|" + user_list[1] + "|" + "0" + "|" + "1" + "\n"
        else:
            newStr += u

    with open("./db/user_info.txt", "w") as f:
        f.write(newStr)


def addBook():
    b_name = input("请输入书名:")
    b_price = input("请输入书的价格:")
    b_total = input("请输入书的总数:")
    b_reste = input("请输入剩余书数量:")

    # 判断用户名是否存在
    with open("./db/books_lib.txt", "r") as f:
        books = f.readlines()




    pass

def modifyBook():
    pass

def deleteBook():
    pass

menu3 = (("退出系统", 3),)
menu2 = (("密码找回", 2), ("退出系统", 3), ("冻结用户", 4), ("添加图书", 5), ("修改图书", 6), ("下架图书", 7))
menu1 = (("会员注册", 0), ("会员登录", 1), ("退出系统", 3))

while True:
    menu = menu1
    if isLogin and usernameOfLogined == "admin":
        menu = menu2
    elif isLogin and usernameOfLogined != "admin":
        menu = menu3

    print("\n\n\n")
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
    elif index == 4:
        freezeUser()
