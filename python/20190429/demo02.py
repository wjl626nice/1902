# 继承
'''
把若干个类中相同的部分抽离出来，形成一个新的类，之前的类来继承于这个新的类
'''


class Animal:

    def eat(self):
        print("{} 吃 ".format(self.name))

    def drink(self):
        print("{} 喝 ".format(self.name))

    def shit(self):
        print("{} 拉 ".format(self.name))

    def pee(self):
        print("{} 撒 ".format(self.name))


class Cat(Animal):

    def __init__(self, name):
        self.name = name
        self.breed = '猫'

    def cry(self):
        print('喵喵叫')


class Dog(Animal):

    def __init__(self, name):
        self.name = name
        self.breed = '狗'

    def cry(self):
        print('汪汪叫')


# ######### 执行 #########
c1 = Cat('小白家的小黑猫')
c1.eat()

c2 = Cat('小黑的小白猫')
c2.drink()

d1 = Dog('胖子家的小瘦狗')
d1.eat()


# 单继承
# 父类
class Person:
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.weight = w

    def speak(self):
        print("{} 说: 我 {} 岁。".format(self.name, self.age))


# 子类
'''
子类中的注意事项：
1.类名后加(父类)
2.如果父类中显示的声明了构造方法，在子类的构造方法中需要调用父类的构造方法

子类在使用方法的时候，先寻找自己类中是否有这个方法，如果没有，那么寻找父类的方法
'''


class Student(Person):
    def __init__(self, n, a, w, g):
        Person.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("{} 说: 我 {} 岁。我在读 {} 年级".format(self.name, self.age, self.grade))


xm = Student("小明", 18, "150", "3")
xm.speak()

