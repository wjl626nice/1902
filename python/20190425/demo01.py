# 集合
'''
集合（set）是一个无序的不重复元素序列

可以使用大括号 { } 或者 set() 函数创建集合，

注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
'''

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

print(basket)

# in
print("apple" in basket)

# 集合运算
a = set('abracadabra')
print(a)
b = set('alacazam')
print(b)

# -     集合a中包含而集合b中不包含的元素
print(a - b)

# |     集合a或b中包含的所有元素
print(a | b)

# &     集合a和b中都包含的所有元素
print(a & b)

# ^     不同时包含于a和b的元素
print(a ^ b)

# 集合支持集合推导式
c = "abcmdkekarftyugbds"
# 迭代 c,判断c中的字符是否不在 "abc", 用不在 "abc" 里面内容形成一个新的集合
d = {x for x in c if x not in 'abc'}

print(d)

# 集合的基本操作
set1 = set(("Google", "Runoob", "Taobao"))
print(set1)

list1 = ["abc", "bcd", "1234", "abc"]
print(list1)
set2 = set(list1)
print(set2)
list2 = list(set2)
print(list2)

# 添加元素  add
set2.add("cp")
print(set2)

set2.add(("fghj", "ghjkl"))
print(set2)

set2.add(123456)
print(set2)

# update
set2.update(["1", "2"])
print(set2)

set2.update(("3", "4"))
print(set2)

set2.update({"4", "5"})
print(set2)

set2.update({"name": "zs", "age": 18})
print(set2)

# 移除元素
set2.remove("age")
print(set2)

# 删除不存在的内容会报异常
# set2.remove("age")
# print(set2)

# discard()
set2.discard("name")
print(set2)

# 删除不存在的内容不会报异常
set2.discard("name")
print(set2)

# 随机删除集合中的一个元素
set2.pop()
print(set2)

# 集合元素个数
print(len(set2))

# 清空集合
set2.clear()
print(set2)

# copy()	拷贝一个集合
set3 = {"cp", "sc", "dy", "ds"}
set4 = set3.copy()
print(set3 == set4)

set3.add("sy")
set4.add("nb")
print(set3)
print(set4)

# difference()	返回多个集合的差集    -
# print(set3.difference(set4))

# difference_update()	移除集合中的元素，该元素在指定的集合也存在。      修改原集合
# set4.difference_update(set3)
# print(set4)


# intersection()	返回集合的交集   &
# print(set3.intersection(set4))

# intersection_update()	删除集合中的元素，该元素在指定的集合中不存在。     修改原集合
# set3.intersection_update(set4)
# print(set3)
#
# set5 = {1, 2}
# set6 = {3, 4}
# print(set5.intersection(set6))


# isdisjoint()	判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
# print(set3.isdisjoint(set4))


set7 = {1, 2, 3, 4, 5, 6}
set8 = {1, 2, 5}
# issubset()	判断指定集合是否为该方法参数集合的子集。
print(set8.issubset(set7))

# issuperset()	判断该方法的参数集合是否为指定集合的子集
print(set7.issuperset(set8))


# symmetric_difference()	返回两个集合中不重复的元素集合。    ^
print(set3.symmetric_difference(set4))

# symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。


# union()	返回两个集合的并集           |
print(set3.union(set4))




