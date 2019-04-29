# 多继承
'''
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>

需要注意圆括号中父类的顺序，两个父类之间用 逗号 隔开
'''


class Person1():
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.weight = w

    def speak1(self):
        print("{} 说: 我 {} 岁。".format(self.name, self.age))


class Student(Person1):
    def __init__(self, n, a, w, g):
        Person1.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak1(self):
        print("{} 说: 我 {} 岁。我在读 {} 年级".format(self.name, self.age, self.grade))


class Speaker(Person1):
    def __init__(self, n, a, w, t):
        Person1.__init__(self, n, a, w)
        self.topic = t

    def speak1(self):
        print("我叫 {}，我是一个演说家，我演讲的主题是 {}".format(self.name, self.topic))


class Sample(Speaker, Student):
    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, a, w, t)

    def speak1(self):
        print("1234567890")


test = Sample("Tim", 25, 80, 4, "Python")
test.speak()

'''
python3中
实例对象在使用方法的时候，
按照广度方式寻找方法，
先在当前类 --> 然后在第一层父类中寻找（第一个继承的父类 --> 第二个继承的父类）
 --> 然后在第二层父类（父类的父类）中寻找 --> ... --> 直到找到最终的祖先类
 
 如果一直找不到 方法，会抛出异常
 
python2中：
新式类：按照广度方式寻找

经典类：按照深度方式寻找
先在当前类 - 第一个继承的父类 - 第一个继承的父类的父类 - 直到把当前分支找完
第二个继承的父类 - 第二个继承的父类的父类 -  直到把当前分支找完
...
'''