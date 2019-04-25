# for循环
'''
for <variable> in <sequence>:
    <statements>
else:
    <statements>
'''

languages = ["C", "C++", "Perl", "Python"]
for la in languages:
    print(la)
else:
    print("没有循环数据!")


# range(开始, 结束, 步进)

for i in range(5):
    print(i)

for j in range(1, 10):
    print(j)

for k in range(1, 10, 2):
    print(k)


# 使用range()创建列表
list1 = list(range(5))
print(list1)

tuple1 = tuple(range(5))
print(tuple1)