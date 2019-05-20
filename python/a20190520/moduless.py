# 相当于匿名函数
getNum = lambda a,b: a+b


# __name__ 直接运行当前文件时输出 __main__ ，如果是模块式被别的文件引入，那么代表当前的模块名

print(__name__)

if __name__ == '__main__':
    # 当前代码只会在当前文件直接运行时，才会执行。
    print('我是moduless模块')
    pass