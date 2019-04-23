# 运算符
# 算术运算符         **(幂运算)   //(除取整)
# 赋值运算符
# 比较运算符
# 逻辑运算符

# 成员运算符
# in
# not in
a = 10
b = 20
list = [1, 2, 3, 4, 5]

if a in list:
    print("a在list中")
else:
    print("a不在list中")

# 身份运算符
'''
身份运算符用于比较两个对象的存储单元
is	is 是判断两个标识符是不是引用自一个对象
is not	is not 是判断两个标识符是不是引用自不同对象
'''

c = 20
d = 20

if (c is d):
    print("c 和 d 有相同的标识")
else:
    print("c 和 d 没有相同的标识")

e = ["1234", "456789"]
f = ["1234", "456789"]

if (e is f):
    print("e 和 f 有相同的标识")
else:
    print("e 和 f 没有相同的标识")

g = f

if (g is f):
    print("g 和 f 有相同的标识")
else:
    print("g 和 f 没有相同的标识")