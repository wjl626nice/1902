# from abcd.aaa import *
import sys

# abca = 1
# abc = 2
# abca()
print(sys.path)
# 引入包,自动执行包下边的__init__文件
import abcd

abcd.aaa.abca()

# 按着command 用鼠标左键点击 urllib  就进入了包
# import urllib
from urllib import request

# request 模块内已经封装了http请求结构体
ret = request.urlopen('http://baidu.com')
print(ret.getcode())
# 读取请求成功的内容
print(ret.read())