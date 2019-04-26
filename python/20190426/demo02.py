# 装饰器
'''
在代码运行期间动态为函数增加功能的方式就叫装饰器。它本身是一种“语法糖”，其本质还是一个函数，
因此我们还可以这样定义它：它是一个装饰其它函数的函数，用来为其它函数动态添加一些额外功能。

装饰器的基本原则

不能修改被装饰函数的源代码
不能修改被装饰的函数的原有调用方式

'''


def ccc(func):
    # 这里我们用可变参数，和关键字参数
    def inner(*args, **dic):
        print('西门大官人')
        func(*args, **dic)

    return inner


def ddd(func):
    # 这里我们用可变参数，和关键字参数
    def inner(*args, **dic):
        print('ddd')
        func(*args, **dic)

    return inner


# 使用ccc函数装饰aaa函数
@ccc
@ddd
def aaa(x, y, **z):
    print(x)
    print(y)
    print(z['name'])


aaa(123, 1111, name='大郎')
