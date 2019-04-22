# 列表相当于 js 中的数组
list = [12, "abc", 789, 0, 56, "阿斯蒂芬规划局快乐"]
print(list[0])
# 列表的截取跟字符串相同
# 变量[头下标:尾下标]
ls1 = list[2:]
print(ls1)
ls2 = list[:3]
print(ls2)
ls3 = list[2:5]
print(ls3)
ls4 = list[-5:-1]
print(ls4)

# 加号 + 是列表连接运算符，星号 * 是重复操作。 跟字符串相同 略


# 字符串中的内容不能修改，列表中内容可以被修改
str1 = "hello"
print(str1[1])
# str1[1] = "E"
# print(str1)


print(list[3])
list[3] = 9
print(list[3])

'''
元组，跟list相似，内容不能被修改，书写的过程中用 () 包裹起来
'''
tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
t1 = tuple[1:]
print(t1)

# tuple[1] = 678
# print(tuple)

tup1 = ()  # 空元组
tup2 = (20,)  # 一个元素，需要在元素后添加逗号

# 元组也可以使用+操作符进行拼接。


