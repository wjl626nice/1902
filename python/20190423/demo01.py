# 数据类型转换
# str() 函数将对象转化为适于人阅读的形式。
persons = [{"name": "张三", "age": 18}, {"name": "李四", "age": 18}, {"name": "王五", "age": 18}]
print(persons)
print(type(persons))
print(type(str(persons)))

# repr() 函数将对象转化为供解释器读取的形式。
print(type(repr(persons)))

# tuple 函数将列表转换为元组。
list1 = ['Google', 'Taobao', 'Runoob', 'Baidu']
tup = tuple(list1)
print(tup)

# 元祖内容不能更改
# tup[0] = "qingyun"
# print(tup)

list1[0] = "qingyun"
print(list1)

# list() 把元组或者字符串转化成 列表
aTuple = (123, 'Google', 'Runoob', 'Taobao')
list1 = list(aTuple)
print("列表元素 : ", list1)

str = "Hello World"
list2 = list(str)
print("列表元素 : ", list2)

# set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等
x = set('runoob')
print(x)
