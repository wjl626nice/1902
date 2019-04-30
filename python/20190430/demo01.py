# 类成员的修饰符

'''
公有成员，在任何地方都能访问
私有成员，只有在类的内部才能方法

私有成员和公有成员的定义不同：
    私有成员命名时，前两个字符是下划线。（特殊成员除外，例如：__init__、__call__、__dict__等）


'''

# 静态字段

# 公有的静态字段
'''
公有静态字段：类可以访问；类内部可以访问；派生类中可以访问
'''


class C:
    name = "公有静态字段"

    def func(self):
        print(C.name)


class D(C):

    def show(self):
        print(C.name)


# 类访问
# print(C.name)

# 类内部可以访问
obj = C()
# obj.func()

# 派生类中可以访问
obj2 = D()
# obj2.show()


# 私有的静态字段
'''
私有的静态字段只能在当前类中使用
'''
class A:
    __name = "私有的静态字段"

    def func(self):
        print(A.__name)


class B(A):

    def show(self):
        print(A.__name)


# print(A.__name)

obj3 = A()
# obj3.func()


obj4 = B()
obj4.show()

