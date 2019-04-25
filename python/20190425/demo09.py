# 函数的返回值为多个值
def fn(n, m):
    result1 = m + n
    result2 = m * n
    return result1, result2


a, b = fn(2, 3)

print(a)
print(b)
