# 文件操作

'''
1.打开文件   open("文件的路径", mode)

2.对于文件的操作

3.关闭文件   close()
'''

# 打开一个文件
# 写     w   从开头开始编辑，即原有内容会被删除,  如果该文件不存在，创建新文件。
# f = open("./tmp/foo.txt", "w")
#
# f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
#
# # 关闭打开的文件
# f.close()


# 读  r   文件的指针将会放在文件的开头, 文件路径有误，会报出异常
f = open("./tmp/foo.txt", "r")

# 读整个文件内容
# str = f.read()
# print(str)

# 按行读取文件，读的是文件对象指针所在行
# str2 = f.readline()
# print(str2)
#
# str3 = f.readline()
# print(str3)


# 读取该文件中包含的所有行
# list4 = f.readlines()
# print(list4)
# print(list4[0])


# 迭代一个文件对象然后读取每行:
# for line in f:
#     print(line, end='')

# print(f.tell())
# str4 = f.readline()
# print(f.tell())

# f.close()


# 如果要写入一些不是字符串的东西, 那么将需要先进行转换:
# f = open("./tmp/foo1.txt", "w")
#
# value = ('www.runoob.com', 14)
# s = str(value)
# f.write(s)
#
# # 关闭打开的文件
# f.close()


'''
f.seek()
如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。

from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：

seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
seek(x,1) ： 表示从当前位置往后移动x个字符
seek(-x,2)：表示从文件的结尾往前移动x个字符

'''
f = open("./tmp/foo2.txt", "rb+")

print(f.write(b'0123456789abcdef'))

print(f.seek(5))
print(f.read(1))

# seek(-x,2)：2表示 从文件的结尾，-x表示 往前移动x个字符
print(f.seek(-3, 2))
print(f.read(1))

print(f.seek(0, 0))
print(f.read(1))

f.close()

while True:
    f = open("./tmp/foo3.txt", "a+")
    un = input("请输入用户名:")
    pwd = input("请输入密码")

    f.write("{}|{}\n".format(un, pwd))
    f.close()
