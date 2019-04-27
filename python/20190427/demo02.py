# 生成器

y = (pow(a, b) for a in range(0, 6) for b in range(1, 3))
print(y)


# 常规函数生成斐波那契数列
def f(n):
    # x 表示前前一个, y表示前一个， z表示当前的一个
    x, y, z = 0, 1, 1
    L = []
    while len(L) < n:
        # 前一个变成 前前一个
        # 当前的变成 前一个
        x, y = y, z
        # 新的当前的等于新的前一个 + 新的前前一个
        z = x + y
        # 将新的前前一个放到列表中
        L.append(x)
    return L


print(f(15))


# yield函数
def f():
    # x 表示前前一个, y表示前一个， z表示当前的一个
    x, y, z = 0, 1, 1
    while True:
        # 前一个变成 前前一个
        # 当前的变成 前一个
        x, y = y, z
        yield x
        # 新的当前的 等于 新的前一个 + 新的前前一个
        z = x + y


fff = f()
print(fff)
# print(next(fff))

# 使用循环遍历生成器
# for i in fff:
#     print('%d\n' % i)


# 有限数量的生成器：

def f(n):
    x, y, z = 0, 1, 1
    L = []
    while len(L) < n:
        x, y = y, z
        yield x
        z = x + y
        L.append(x)


fff = f(15)

# 使用循环遍历生成器
for i in fff:
    print(i)

# 对于有限数量的生成器，使用 next()调用的时候，如果超出边界，会抛出异常，而使用遍历则不会抛出异常
mmm = f(3)
print(next(mmm))
print(next(mmm))
print(next(mmm))
# print(next(mmm))


print("-----------内存比较------------")
import sys

# 无论15个还是150000个，其实内存使用无变化
fff = f(10000)
print(sys.getsizeof(fff))

ggg = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
print(sys.getsizeof(ggg))