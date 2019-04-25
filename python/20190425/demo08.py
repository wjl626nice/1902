# 变量作用域
'''
程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。
变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python的作用域一共有4种，分别是：

L （Local） 局部作用域
E （Enclosing） 闭包函数外的函数中
G （Global） 全局作用域
B （Built-in） 内置作用域（内置函数所在模块的范围）

以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内置中找。
'''

num1 = 10
num2 = 9


def outer():
    num1 = 8
    print(num1)
    print(num2)


outer()

'''
    在上面的例子中 在全局作用域中有两个变量    num1 和 num2,
    在 outer 函数的局部作用域中有一个变量 num1, 在outer 函数中使用 num1 是 局部作用域中的num1,使用 num2 的时候，
    局部作用域中没有num2,就会去全局作用域中寻找
    
    局部作用域 --> 全局作用域
'''

print("--------有闭包作用域---------")
num3 = 88
num4 = 66


def outer():
    num5 = 99

    def inner():
        num6 = 100
        num4 = 999
        print(num6)
        print(num5)
        print(num4)
        print(num3)

    return inner


enclosing = outer()

enclosing()

'''
作用域链  局部作用域 --> 闭包函数外的函数的作用域 --> 全局作用域
'''

# 在模块，类，函数中会形成新的作用域，其他的代码块不会形成新的作用域

if 1:
    b = "阿斯蒂芬规划局快乐"
    print(b)

print(b)

print("--------------global---------------")

# global

num = 1


def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)

    num = 123
    print(num)


fun1()
print(num)

'''
不能直接在函数内部修改全局作用域中的变量，如果想要修改，需要使用 global 关键字声明
'''

# 要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了

print("--------------nonlocal---------------")


def outer():
    m = 10

    def inner():
        nonlocal m  # nonlocal关键字声明
        m = 100
        print(m)

    inner()
    print(m)


outer()