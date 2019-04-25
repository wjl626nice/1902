# 不定长参数 函数
'''
你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名。基本语法如下：
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
'''


def printinfo(*vartuple):
    """打印任何传入的参数"""
    print("输出: ")
    # print(arg1)
    print(vartuple)


printinfo(1, 2, 3, 4, 5, 6, 7, 8)
printinfo()

'''
还有一种就是参数带两个星号 **基本语法如下
def functionname([formal_args,] **var_args_dict ):
   "函数_文档字符串"
   function_suite
   return [expression]
'''
print("----------传入的参数以字典方式显示-----------")


def printinfo(arg1, **vardict):
    """打印任何传入的参数"""
    print("输出: ")
    print(arg1)
    print(vardict)


# 调用printinfo 函数
printinfo(1, a=2, b=3)


# 如果单独出现星号 * 后的参数必须用关键字传入。

def f(a, b, *, c, d):
    return a + b + c + d


print(f(1, 2, c=10, d=20))
# print(f(1, 2, 10))


# 匿名函数
'''
使用 lambda 来创建匿名函数。
lambda 只是一个表达式，函数体比 def 简单很多
不需要换行，也不需要return
形参定义的时候，不需要()

lambda 函数的语法只包含一个语句，如下：

lambda [arg1 [,arg2,.....argn]]:expression
'''

cj = lambda arg1, arg2: arg1 * arg2

print(cj(2, 3))

'''
return  表示函数的结束，return所在代码块中，return语句下面的语句都不会执行
不带参数值的return语句返回None
'''


def fn3():
    pass


print(fn3())