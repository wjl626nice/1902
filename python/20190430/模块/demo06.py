import a.a1

a.a1.fn1()
a.a1.fn2()

# as 重新命名
import a.a2 as abc

abc.fn1()
abc.fn2()

# 从 a.a3 模块中导入所有方法和属性
from a.a3 import *

a.a3.fn1()
a.a3.fn2()

# 从 a.a4 模块中导入 fn1
from a.a4 import fn1

fn1()
# 下面这种方式不能使用 a.a4 模块中的 fn2
# fn2()
