# 集合,内容不重复
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)

# 成员测试
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)
print(b)

# a 和 b 的差集, b - a  表示 b 中有，a 中有
print(b - a)

# a 和 b 的并集  a | b  表示两个集合合并，并去重
print(a | b)

# a 和 b 的交集  a & b  表示两个集合中都有的内容
print(a & b)

# a 和 b 中不同时存在的元素
print(a ^ b)
# print((a - b) | (b - a))




