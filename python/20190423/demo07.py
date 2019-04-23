# 元组
'''
    Python 的元组与列表类似，不同之处在于元组的元素不能修改。
    元组使用小括号，列表使用方括号。
    元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。

    tup1 = ();

    元组中只有一个内容
    tup2 = (1,);

    标索引从0开始，可以进行截取，组合等
'''

# 访问元组跟list相同
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)

print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

# 以下修改元组元素操作是非法的。
# tup1[0] = 100


# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
print(tup1)
del tup1
# print(tup1)

'''
len(tup)                长度
a in tup1               判断某个内容是否在元组中
for x in tup2           使用for in 迭代 tup2
'''

'''
+ , * 会形成新的元组
'''
tup3 = (1, 2, 3, 4, 5, 6)
tup4 = ("a", "b", "c")
tup5 = tup3 + tup4
print(tup5)

tup6 = tup4 * 3
print(tup6)

'''
len(tuple)
计算元组元素个数。

max(tuple)
返回元组中元素最大值。

min(tuple)
返回元组中元素最小值。

tuple(seq)
将列表转换为元组。
'''
