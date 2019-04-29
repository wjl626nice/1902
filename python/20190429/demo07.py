# 静态字段方式
class Foo:

    # getter
    def get_bar(self):
        print("getter Bar")
        return 'Leo'

    # *必须两个参数
    # setter
    def set_bar(self, value):
        print("setter Bar")
        return 'set value' + value

    # deleter
    def del_bar(self):
        print("deleter Bar")
        return 'Leo'

    BAR = property(get_bar, set_bar, del_bar, '对于属性的说明信息')

obj = Foo()

print(obj.BAR)

obj.BAR = "12345"

del obj.BAR