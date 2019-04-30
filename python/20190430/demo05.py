# hasattr, getattr, setattr, delattr
'''
类的反射：可以通过字符串的方式操作对象的成员
'''
class Foo:

    def __init__(self):
        self.name = "1902"

    def fn(self):
        print("Foo普通方法1")

    def fn2(self):
        print("Foo普通方法2")

    def fn3(self):
        print("Foo普通方法3")


obj = Foo()
# hasattr   判断对象是否包含成员
print(hasattr(obj, "name"))
print(hasattr(obj, "age"))
print(hasattr(obj, "fn"))

# getattr
print(getattr(obj, "name"))
print(getattr(obj, "fn"))
# print(getattr(obj, "age"))

# getattr(obj, "fn")()

arg = "fn5"
if hasattr(obj, arg):
    getattr(obj, arg)()


setattr(obj, "name", "python")

print(getattr(obj, "name"))

delattr(obj, "name")
# print(getattr(obj, "name"))
