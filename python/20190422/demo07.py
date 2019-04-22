# 声明 类 A
class A:
    pass


# 声明 类 B 继承于 A
class B(A):
    pass


# 实例化一个 A 类型的对象 a
a = A()

# 实例化一个 B 类型的对象 b
b = B()

'''
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
'''
# isinstance(a A) 判断 a是否是A类型
print(isinstance(a, A))
print(type(a) == A)


# isinstance(b, B) 判断 b是否是B类型
print(isinstance(b, B))
print(type(b) == B)

print(type(b) == A)

