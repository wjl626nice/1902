# datetime
# 从 datetime 模块中导入 datetime 类
from datetime import datetime
now = datetime.now()
print(now)
print(type(now))

dt = datetime(2015, 4, 19, 12, 20)
print(dt)

# 转换成时间戳
ts = dt.timestamp()
print(ts)

# 使用datetime提供的fromtimestamp()方法：
a = float("1429417200.0")
print(a)
dt2 = datetime.fromtimestamp(a)
print(dt2)




