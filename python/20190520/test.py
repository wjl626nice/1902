# 当 import一个模块时 相当于运行了模块内的代码
import sys

# pycharm报错，而python解释器运行不报错。
# pycharm软件会从sys.path中找 sys.path = ['/Users/qingyun/1902/python', '/Applications/PyCharm.app/Contents/helpers/pycharm_display', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python37.zip', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages', '/Applications/PyCharm.app/Contents/helpers/pycharm_matplotlib_backend']
# 当python解释器运行起来时，会把当前文件所在的目录放入到sys.path =['/Users/qingyun/1902/python/20190520', '/Users/qingyun/1902/python', '/Applications/PyCharm.app/Contents/helpers/pycharm_display', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python37.zip', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages', '/Applications/PyCharm.app/Contents/helpers/pycharm_matplotlib_backend']
import moduless


print(sys.path)
print(__name__)
print(moduless.getNum(2, 6))
