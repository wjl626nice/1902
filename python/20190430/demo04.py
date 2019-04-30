# isinstance(obj, cls)
# 判断对象是否是某个类型（当前对象类型，也包含父类类型）
class A:
    def fn1(self):
        pass


class B(A):
    def __init__(self, n):
        self.name = n

    def fn2(self):
        pass


b = B("Leo")
print(isinstance(b, B))

print(isinstance(b, A))


# issubclass(sub, super)
# 判断 某个类是否是另一个类的子类

print(issubclass(B, A))

# type()
# 获取某个对象的类型
print(type(b))
