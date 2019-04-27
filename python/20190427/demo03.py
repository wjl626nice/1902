# 输入输出
# 输入 input

# 输出
# print(), write, 、、、
# 输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))

# 指定位置
print('{1} 和 {1}'.format('Google', 'Runoob', "大表哥真帅"))

#  format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数。
print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))

# 位置和关键字
print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))

# '!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
# print("{!a}{!s}".format("abc", [1, 2, 3]))

import math

# :.3f 保留小数点后3位
print('常量 PI 的值近似为 {0:.5f}。'.format(math.pi))

# : 后跟整数，表示可以保证该域至少有这么多的宽度
table = {'Google': 1, 'Runoobfg': 2001, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ==> {1:10}'.format(name, number))


# 使用方括号 '[]' 来访问键值
print('Runoob: {1[Runoobfg]:10d}; Google: {0[Google]:10d}; Taobao: {0[Taobao]:10d}'.format(table, {'Google': 1, 'Runoobfg': 1999, 'Taobao': 3}))

#  table 变量前使用 '**' 来实现相同的功能：
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))