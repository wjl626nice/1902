import pymysql

# 打开数据库连接
db = pymysql.connect("192.168.9.191", "Leo", "123456789", "python1902")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 删除语句
sql1 = "DELETE FROM good WHERE goods_id = 1"

sql2 = "UPDATE goods SET click_count = 1 WHERE goods_id = 4"

try:
    # 执行SQL语句
    cursor.execute(sql1)
    cursor.execute(sql2)
    # 提交修改
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭连接
db.close()
