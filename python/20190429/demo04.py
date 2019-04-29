# 字段

'''
静态字段，普通字段
    书写位置：
        静态字段直接书写在类中，
        普通字段书写在 类的构造方法中

    存储位置：
         静态字段存储在类中，只保存一份
         普通字段存储在实例化对象中，每一个对象都有一份

    访问方式：
        普通字段 只能通过实例对象访问
        静态字段既能通过类名访问，也能通过实例对象访问，
        但是通过实例对象访问静态字段的时候，只能获取值，不能更改
'''
class Province:
    # 静态字段
    country = '中国'

    def __init__(self, n):
        # 普通字段
        self.name = n


# 直接访问普通字段
obj = Province('河北省')
print(obj.name)

# 直接访问静态字段
# print(Province.country)

# 普通的字段不能通过类名直接访问
# print(Province.name)
# print(obj.country)

obj2 = Province("河南省")
print(obj2.name)


# 两个对象访问的静态字段是同一个
print(obj.country)
print(obj2.country)

# 通过类来更改静态字段
Province.country = "中华人民共和国"

print(obj.country)
print(obj2.country)

obj3 = Province("山东省")
print(obj3.country)

# 下面这种方式，不是更改静态字段，而是，在 obj 对象上添加一个新的普通字段
obj.country = "usa"
# 下面这个 访问的是 obj 的普通字段
print(obj.country)
# 下面这个 访问的是 obj2 指向的类的静态字段
print(obj2.country)

