import pymysql

# 打开数据库连接
# pymysql.connect(地址, 用户名称, 密码, 数据库名称)
dbcon = pymysql.connect("192.168.9.191", "Leo", "123456789", "python1902")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = dbcon.cursor()

# 使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT VERSION()")
cursor.execute("SELECT * from goods")

# 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchall()
data = cursor.fetchone()
# data = cursor.fetchmany(2)
# print("Database version : %s " % data)
print(data)

# 关闭数据库连接
dbcon.close()