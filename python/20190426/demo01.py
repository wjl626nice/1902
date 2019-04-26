# 函数对象
def ss(x):
    print(x + 1)


print(ss)

xxx = ss

print(xxx)

print(xxx == ss)

ss = 1234
print(ss)

# ss(10)
xxx(10)


# map(def, 可迭代的对象)
def fn1(x):
    return x * x


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
map2 = map(fn1, list1)
list2 = list(map2)
print(list2)

# reduce()

# 从 functools 模块中 reduce 导入
from functools import reduce


# 把 functools 模块导入
# import functools
def f(x, y):
    return x + y


l = reduce(f, [2, 4, 6, 10])
print(l)

l2 = reduce(f, range(1, 10))
print(l2)


# filter()

# 筛选出偶数
def get_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


fl1 = filter(get_even, range(0, 10))
list3 = list(fl1)
print(list3)

list4 = [{"name": "长朋", "age": 18, "height": 180},
         {"name": "nc", "age": 17, "height": 178},
         {"name": "苏晨", "age": 20, "height": 160},
         {"name": "sy", "age": 24, "height": 170},
         {"name": "dd", "age": 30, "height": 179},
         {"name": "nb", "age": 29, "height": 176}]


def fn4(person):
    return person["height"] >= 175


list5 = filter(fn4, list4)
print(list(list5))

# sorted()
'''
列表(list)自带的有排序方法list.sort()，排序方式和sorted()基本一样，
不过list.sort()操作的是元列表，而sorted()排序后生成的是个新的列表。
'''
list6 = [1, 3, 9, 2, -2, 90, 10]
# 升序
# list7 = sorted(list6)
# print(list6)
# print(list7)
#
# list6.sort(reverse=True)
# print(list6)


# 倒序
list8 = sorted(list6, reverse=True)
print(list8)

list9 = [('如花', 99), ('小花', 35), ('小明', 66), ('张三', 40)]


def xxx(x):
    print("--------------")
    print(x)
    return x[1]


list10 = sorted(list9, key=xxx, reverse=True)
print(list10)

list11 = [{"name": "长朋", "age": 18, "height": 180},
          {"name": "nc", "age": 17, "height": 178},
          {"name": "苏晨", "age": 17, "height": 160},
          {"name": "sy", "age": 24, "height": 170},
          {"name": "dd", "age": 30, "height": 179},
          {"name": "nb", "age": 29, "height": 176}]


def fn7(p):
    return p["age"]


list12 = sorted(list11, key=fn7)
print(list12)

def fn8(p):
    return p["height"]


list13 = sorted(list11, key=fn8, reverse=True)
print(list13)
