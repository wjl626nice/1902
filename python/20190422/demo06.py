# 行与缩进
# 行和缩进来表示代码块    在python中不需要{}来表示代码块
if 7 < 5:
    print("哈哈")
else:
    print("呵呵")


# 定义函数
def sum(n1, n2):
    return n1 + n2


print(sum(1, 2))

# 数字类型的数据
'''
    整数，浮点数，布尔型，复数（选学）
    
    注意事项：True == 1, False == 0
'''

a = True
b = False

if a == 1:
    print("True == 1")

if b == -1:
    print("False == 0")

"""
    字符串：
        使用单引号和双引号包裹起来的字符
        使用三引号('''或\""")可以指定一个多行字符串。
        
        字符串可以用 + 运算符连接在一起,用 * 运算符重复
        
        Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
        
        字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
        
"""
name = "张三"

introduce = """我是一个\n大帅哥，
每天都被自己帅醒，
我真的好累呀       
"""
print(introduce)

str = name + introduce
print(str)

str2 = str * 2
print(str2)

str3 = "不为模糊不清的未来担忧，只为清清楚楚的现在努力"
str4 = str3[1::]
print(str4)

# 用户输入

# message = input("请输入你的用户名：")
# print(message)

# 在同一行输入多行语句，不建议使用
# import sys; x = 'runoob'; sys.stdout.write(x + '\n')

# 缩进相同的一组语句构成一个代码块，我们称之代码组。
if 7 < 5:
    print("哈啊哈")
    print("🙄")

'''
 print  在python2 中直接使用，后面跟需要输出的内容
        在python3 中需要 包含在 () 中
'''

# 变量赋值
# 常规赋值 略
# 为多个对象指定多个变量
a, b, c = 1, 2, "帅哥"
print(a, c, b)
