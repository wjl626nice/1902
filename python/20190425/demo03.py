# 循环语句有 for 和 while。
'''
while 判断条件：
    语句

一般情况下使用在 未知循环次数的情况下
Python中没有do..while循环。
'''

n = 100

sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为: %d" % (n, sum))

# 无限循环      一般情况下，不使用，
# var = 1
# while var == 1:  # 表达式永远为 true
#     num = int(input("输入一个数字  :"))
#     print("你输入的数字是: ", num)
#
# print("Good bye!")


# while else            当while语句中的条件不成立的时候执行else语句中的内容
count = 0
while count < 5:
    print(count, " 小于 5")
    count = count + 1
else:
    print(count, " 大于或等于 5")

# 简单语句组
flag = 1
while (flag): print('欢迎访问菜鸟教程!')
print("Good bye!")
