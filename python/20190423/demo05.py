# 字符串内建函数
'''

capitalize()
将字符串的第一个字符转换为大写

'''
a = "hello"
print(a.capitalize())

'''
center(width, fillchar)
返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
'''
b = a.center(30, "*")
print(b)

'''
count(str, beg= 0,end=len(string))
返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
'''
c = "*"

'''
encode(encoding='UTF-8',errors='strict')
以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
'''
str = "我爱你中国abc"

print(str)
print(str.encode(encoding="utf-8"))

'''
bytes.decode(encoding="utf-8", errors="strict")
Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。
'''
byte = str.encode(encoding="utf-8")
print(byte.decode(encoding="utf-8"))

'''
find(str, beg=0, end=len(string))
检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
'''

d = "helloworld"
e = d.find("world1")
print(e)

'''
index(str, beg=0, end=len(string))
跟find()方法一样，只不过如果str不在字符串中会报一个异常.
'''
# f = d.index("world1")
# print(f)

'''
isalnum()
如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False


isalpha()
如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False

isdigit()
如果字符串只包含数字则返回 True 否则返回 False..

'''

g = "1234567d"
print(g.islower())

h = "1234567dQ"
print(h.islower())

'''
join(seq)
以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
'''
ls = ["abc", "234", "678", "ghj"]
i = "*"
j = i.join(ls)
print(j)

'''
len
字符串的长度
'''
print(len(j))

'''
	
split(str="", num=string.count(str))
num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串
'''
ls2 = j.split("*")
print(ls2)

'''
splitlines([keepends])
按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
'''

str2 = '''leo|123456|boy\ncp|123456|boy\ndd|123456|boy'''
print(str2)

ls3 = str2.splitlines()
print(ls3)



