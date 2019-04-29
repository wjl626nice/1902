# 面向对象编程
'''
参考地址:http://www.cnblogs.com/wupeiqi/p/4493506.html

面向对象编程是一种编程方式，此编程方式的落地需要使用 “类” 和 “对象” 来实现，
所以，面向对象编程其实就是对 “类” 和 “对象” 的使用。

类就是一个模板，模板里可以包含多个函数，函数里实现一些功能
对象则是根据模板创建的实例，通过实例对象可以执行类中的函数
'''


# 声明创建一个类
class Foo:

    def Bar(self):
        print("bar")

    def Hello(self, name):
        print("I am {}".format(name))


# 实例化对象
obj = Foo()
print(obj)

# 通过对象使用方法
obj.Bar()
obj.Hello("大表哥")


# 封装，把数据封装在类中，使用类的作用域
'''
  __init__ 是类的构造方法，当使用类实例化一个对象的时候，会默认调用该方法，
  该方法中的第一个参数，指的是将要返回的新的实例化对象  
'''
class Foo2:
    def __init__(self, n, a):
        # print('实例化一个Foo2对象')
        self.name = n
        self.age = a

    def Hello(self):
        # 通过self间接调用被封装的内容
        print("I am {}, age: {}".format(self.name, self.age))


obj2 = Foo2("Leo", 18)
# 通过对象直接调用被封装的内容
print(obj2.name)
print(obj2.age)
obj2.Hello()

print("---------------------------------------------")
# 砍柴，去东北，大保健
class Person:
    def __init__(self, n, a, s):
        self.name = n
        self.age = a
        self.sex = s

    def kanchai(self):
        print("我是{},今年{}岁,性别：{},我要去砍柴，换成钱".format(self.name, self.age, self.sex))

    def qudongbei(self):
        print("我是{},今年{}岁,性别：{},我开车去东北".format(self.name, self.age, self.sex))

    def dabaojian(self):
        print("我是{},今年{}岁,性别：{},我拿着柴钱，来大保健".format(self.name, self.age, self.sex))


# 实例化对象
xm = Person("小明", 18, "男")
xm.kanchai()
xm.qudongbei()
xm.dabaojian()

laoli = Person("老李", 78, "男")
laoli.kanchai()
laoli.qudongbei()
laoli.dabaojian()