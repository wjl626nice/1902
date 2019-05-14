import urllib.request as req
import socket

# str = 'adfasdfa是'
# encode 从字符串转换成字节
# decode 从字节转换成字符串
# print(str, type(str), str.encode('utf-8'))

res = req.urlopen('http://www.cnblogs.com/evablogs/p/6709707.html')
# 获取指定网址的内容
content = res.read().decode('utf-8')
# 打开一个文件，不存在创建
file = open('test.html', 'x')
# 向打开的文件内写入内容
file.write(content)
# 关闭文件
file.close()