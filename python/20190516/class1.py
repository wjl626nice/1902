# 默认继承了object类（对象）

class aa:
    def aaaa(self):
        print('aaaa')

class bb:
    def bbbb(self):
        print('bbbb')

class cc:
    def cccc(self):
        print('cccc')

# abc类继承了aa类
# class abc(aa):
# abc类继承了aa, bb, cc类
class abc(aa, bb, cc):
    def __init__(self, name, age=23):
        # 初始化方法
        self.name = name
        self.age = age

    def get(self,ab):
        print(ab)

    def abc(self):
        print('abc')
    # def __str__(self):
    #     # 双下方法，自动触发（当对象被作为字符串时）
    #     return self.name

    def __eq__(self, other):
        # 当对象发生对比操作时 自动触发。可以自定义对比对象的属性
        if self.name == other.name:
            return True
        else:
            return False

#  abc() 实例化上边的abc类，会自动触发内部的   __init__ 方法
abcc = abc('鑫鑫')  # abcc 就是abc类实例化后产生的对象

print(dir(abcc))

# print 打印字符串
print(abcc, abcc.name)  # <__main__.abc object at 0x10de54470>  内存地址0x10de54470，如果在对象内部定义了__str__方法时会自动触发。

# a = 110111000000000000122211
# b = 110111000000000000122211
# print(id(a), id(b))

abcd = abc('鑫鑫')
print(id(abcc), id(abcd))
print(abcc == abcd)  # 会自动触发__eq__