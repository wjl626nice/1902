from functools import wraps

def decorator(func):
    @wraps(func)  # 修复装饰器
    def inner(*args, **kwargs):
        """
        我是闭包函数
        :param args:
        :param kwargs:
        :return:
        """
        print('鹏祥')
        func()
        print('瑞磊')

    return inner

@decorator
def test():
    """
    我是测试函数
    :return:
    """
    print('淙琳')


test()

print(test.__name__, test.__doc__)