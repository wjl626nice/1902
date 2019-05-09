import pymysql

# 打开数据库连接
db = pymysql.connect("192.168.9.191", "Leo", "123456789", "Library")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 删除语句
sql1 = "DELETE FROM good WHERE goods_id = 1"

sql2 = "UPDATE goods SET click_count = 1 WHERE goods_id = 4"

sql3 = "insert into user_info (u_name, u_pwd, u_email) values ('wjl','112211','wangjl626@live.com')"

try:
    # 执行SQL语句
    # cursor.execute(sql1)
    # cursor.execute(sql2)
    cursor.execute(sql3)
    # 提交修改
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭连接
db.close()
