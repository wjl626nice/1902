# continue, break, pass

# break 跳出循环
for letter in 'Runoob':  # 第一个实例
    if letter == 'o':
        break
    print('当前字母为 :', letter)

# continue 跳过当前这次循环
for letter in 'Runoob':  # 第一个实例
    if letter == 'n':  # 字母为 n 时跳过输出
        continue
    print('当前字母 :', letter)

# pass是空语句，是为了保持程序结构的完整性
print("------pass--------")
for letter in 'Runoob':
    if letter == 'o':
        pass
    else:
        print('当前字母 :', letter)

# 逢七过
for i in range(1, 100):
    if i % 7 == 0 or "7" in str(i):
        print("过")
    else:
        print(i)

print("-------素数--------")

# 循环嵌套
# 质数定义为在大于1的自然数中，除了1和它本身以外不再有其他因数
i = 2
while i < 100:
    j = 2
    while j < i:
        if i % j == 0:
            break
        j += 1
    else:
        print(i)
    i += 1
