# 修饰符，在普通字段中的使用
# 公有的普通字段
class C:

    def __init__(self):
        self.foo = "公有字段"

    def func(self):
        # 类内部访问
        print(self.foo)


class D(C):

    def show(self):
        # 派生类中访问
        print(self.foo)


obj = C()
# 通过对象访问
# print(obj.foo)
# 类内部访问
# obj.func()
#
# 在派生类中访问
obj_son = D()
# obj_son.show()
# print(obj_son.foo)


# 私有的普通字段
'''
私有的普通字段，只能在当前类中使用
'''
class A:
    name = "Leo"
    def __init__(self):
        self.__foo = "私有字段"

    def func(self):
        # 类内部访问
        print(self.__foo)

    def __str__(self):
        return str(self.__dict__)


class B(A):

    def show(self):
        # 派生类中访问
        print(self.__foo)


obj_A = A()
# 对象不能使用私有字段
# print(obj_A.__foo)
# 类内部通过self间接使用
# obj_A.func()


obj_B = B()
# print(obj_B.__foo)
# obj_B.show()


print(A.__doc__)

print(obj_A.__class__)

print("----------------------------------")
print(A.__dict__)
print("----------------------------------")
print(obj_A.__dict__)
print("----------------打印对象------------------")
print(obj_A)