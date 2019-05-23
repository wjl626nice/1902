import os

# 当前文件的物理路径
print(__file__)
# 文件所在的绝对路径
print(os.path.abspath(__file__))
# 获取文件所在的目录
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# window \r \n
# linux  \n
print(os.linesep)

print(os.sep)  #  获取当前系统的目录分隔符