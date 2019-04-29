# 属性
'''
定义时，在普通方法的基础上添加 @property 装饰器；
定义时，属性仅有一个self参数
调用时，无需括号
           方法：foo_obj.func()
           属性：foo_obj.prop
'''


# ############### 定义 ###############
class Foo:

    def func(self):
        print("一个普通函数")
        pass

    # 定义属性
    @property
    def prop(self):
        print("一个属性")
        pass


# ############### 调用 ###############
foo_obj = Foo()

# 调用函数
foo_obj.func()

# 调用属性
foo_obj.prop


# 分页器
class Pager:

    def __init__(self, current_page):
        # 用户当前请求的页码（第一页、第二页...）
        self.current_page = current_page
        # 每页默认显示10条数据
        self.per_items = 10

    @property
    def start(self):
        val = (self.current_page - 1) * self.per_items
        return val

    @property
    def end(self):
        val = self.current_page * self.per_items
        return val


p = Pager(3)
print(p.start)
print(p.end)


class Goods(object):
    def __init__(self, n, p):
        self.name = n
        self.__p = p

    @property   # getter
    def price(self):
        print('@property')


        return self.__p

    @price.setter
    def price(self, value):
        print('@price.setter')


        self.__p = value

    @price.deleter
    def price(self):
        print('@price.deleter')

        del self.__p


print("-----------------------------")
obj = Goods("华为手机", 5999)

# 获取obj对象的属性 price
print(obj.price)

# obj.price = 1234
# print(obj.price)

# del obj.price
# print(obj.price)

# print(obj.__p)