# 数学函数
'''
    求绝对值                abs
    向下取整                floor
    向上取整                ceil
    最大值                  max
    最小值                  min
    四舍五入                round
    平方根                  sqrt

    比较两个数字大小         (x>y)-(x<y)   x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
'''

a = 10
b = 10

print((a > b) - (a < b))

print(max(1, 2, 3, 4, 5, 6, 7, 9))
print(min(1, 2, 3, 4, 5, 6, 7, 9))
print(round(4.51, 1))

import math

print(math.sqrt(9))

'''
    随机数
    random
'''
import random

c = random.random()
print(c)

ls = range(100)
print(ls)
print(random.choice(range(100)))

print("从列表中 [1, 2, 3, 5, 9]) 返回一个随机元素 : ", random.choice([1, 2, 3, 5, 9]))
print("从字符串中 'Runoob' 返回一个随机字符 : ", random.choice('Runoob'))

# shuffle 打乱列表
list = [20, 16, 10, 5];
random.shuffle(list)
print("随机排序列表 : ", list)

random.shuffle(list)
print("随机排序列表 : ", list)

# 格式化字符串
'''
    %s         格式化字符串
    %d         格式化整数
'''
print("我叫 %s 今年 %d 岁! 性别 %s" % ('小明', 10, "男"))
