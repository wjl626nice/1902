# .元素分类 有如下值列表 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中
list1 = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]


# list2 = []
# list3 = []
# for x in list1:
#     if x >= 66:
#         list2.append(x)
#     else:
#         list3.append(x)

dict1 = {"k1": list2, "k2": list3}
print(dict1)


# filter 函数 可以自定义规则过滤列表中的内容，返回值是 filter object
def gteq66(x):
    return x >= 66


list2 = filter(gteq66, list1)


def lt66(x):
    return x < 66


list3 = filter(lt66, list1)

dict1 = {"k1": list2, "k2": list3}
print(dict1)

print(dict1["k1"].__next__())
print(dict1["k1"].__next__())
print(dict1["k1"].__next__())
print(dict1["k1"].__next__())
print(dict1["k1"].__next__())


print(dict1["k2"].__next__())
print(dict1["k2"].__next__())
print(dict1["k2"].__next__())
print(dict1["k2"].__next__())
print(dict1["k2"].__next__())


