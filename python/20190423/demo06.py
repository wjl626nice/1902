# 列表，
'''
有序的数据集合，
索引要从0开始，
内容可以改变
'''

list1 = ["a", "b", "c", "d"]
# 访问值
print(list1[0])
# [start:end]   从start开始，不包含 end
print(list1[1:4])

# 更新列表
list1[3] = "third"
print(list1)

# 删除列表元素
del list1[2]
print(list1)

# 列表脚本操作符
# len
print(len(list1))

print("----------加号---------")
# +
ls11 = [1, 2, 3]
ls12 = ["a", "b"]
ls13 = ls11 + ls12
print(ls13)

# *
print("----------乘号---------")
ls14 = ls12 * 3
print(ls14)

# in, not in
print(2 in [1, 2, 4, 5])

# for in
for x in [1, 2, 4, 5][0:3]:
    print(x)

'''
列表，
    索引顺序 
        从左到右  从 0 开始，依次递增
        从右到左  从 -1 开始，依次递减
'''
print([1, 2, 4, 5][2])
print([1, 2, 4, 5][-2])

print([1, 2, 4, 5, 6, 8][1:])
print([1, 2, 4, 5, 6, 8][1:3])
print([1, 2, 4, 5, 6, 8][:4])
print([1, 2, 4, 5, 6, 8][:])

list2 = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]
print(list2[2])
print(list2[2][2])

for x in list2:
    print(x)
    for y in x:
        print(y)

print("---------列表函数----------------")
'''
len(list)
列表元素个数

max(list)
返回列表元素最大值

min(list)
返回列表元素最小值


list(seq)
将元组转换为列表
'''
tuple1 = (1, 2, 3, 4, 5)
# tuple[2] = 10
print(tuple1)

list3 = list(tuple1)
list3[2] = 10

print(list3)

tuple2 = tuple(list3)
print(tuple1)
print(tuple2)

print("---------列表方法----------------")

'''
list.append(obj)
在列表末尾添加新的对象
'''
list4 = [6, 4, 6, 7, 2, 9]
list4.append("leo")
print(list4)

# 把列表当成一个整体 追加到 原列表中
list4.append([1, 3, 6, 5])
print(list4)

'''
list.count(obj)
统计某个元素在列表中出现的次数
'''
print(list4.count(6))

'''
list.extend(seq)
在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
'''
print(list4)
list4.extend([1, 2, 3, 4, 5, 6])
print(list4)

# 语言列表
language = ['French', 'English', 'German']

# 元组
language_tuple = ('Spanish', 'Portuguese')

# 集合
language_set = {'Chinese', 'Japanese'}

# 添加元组元素到列表末尾
language.extend(language_tuple)
print('新列表: ', language)

# 添加集合元素到列表末尾
language.extend(language_set)
print('新列表: ', language)

# print(list4 + language_tuple)

'''
list.index(obj)     找不到会报异常
从列表中找出某个值第一个匹配项的索引位置
'''
print([1, 2, 3, 4, 5, 6].index(3))
# print([1, 2, 3, 4, 5, 6].index(8))

'''
list.insert(index, obj)
将对象插入列表
'''
list5 = [1, 2, 3, 4, 5]
list5.insert(2, "a")
print(list5)

list5.insert(2, {"d", "e"})
print(list5)

'''
list.pop([index=-1])
移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
'''
list5.pop()
print(list5)

'''
list.remove(obj)
移除列表中某个值的第一个匹配项
'''
list5.remove(1)
print(list5)

list5.remove("a")
print(list5)

list5.remove({"d", "e"})
print(list5)

list5 += [5, 6, 5]
print(list5)

list5.remove(5)
print(list5)

'''
list.reverse()
反向列表中元素
'''
list5.reverse()
print(list5)

'''
list.sort( key=None, reverse=False)
对原列表进行排序
'''
list5.sort()
print(list5)
list5.sort(key=None, reverse=True)
print(list5)

list6 = [{"name": "zs", "age": 18}, {"name": "ls", "age": 21}, {"name": "ww", "age": 17}, {"name": "zl", "age": 28},
         {"name": "tq", "age": 16}]
print(list6)


# 获取列表的第二个元素
def takeKey(elem):
    return elem["age"]


list6.sort(key=takeKey, reverse=False)
print(list6)

'''
list.clear()
清空列表
'''
# list6.clear()
# print(list6)


'''
list.copy()
复制列表
'''
list7 = list6.copy()
print(list6)
print(list7)
print(list6 == list7)

list7[1]["age"] = 18
print(list7)
print(list6)

print("------------copy模块-----深拷贝-------")
import copy

# copy.deepcopy()   深拷贝
list8 = copy.deepcopy(list6)
print(list6)
print(list8)

print(list6 == list8)
list8[1]["age"] = 19
print(list6 == list8)

print(list6)
print(list8)

print("------------copy模块----浅拷贝--------")
# copy.copy()   浅拷贝
list9 = list6
print(list6)
print(list9)

print(list6 == list9)
list9[1]["age"] = 19
print(list6 == list9)

print(list6)
print(list9)

