from flask import Flask
import pymysql
import os,sys
import json
from model.Category import Category

# 获取当前文件所在的目录
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, BASE_DIR)

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/api/articles')
def article():
    # 连接database
    conn = pymysql.connect(host='127.0.0.1', user="root", password='123456', database="myblog",
    charset='utf8')
    # 得到一个可以执行SQL语句的光标对象
    # cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示

    # 得到一个可以执行SQL语句并且将结果作为字典返回的游标
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    sql = "select * from blog_category"
    cursor.execute(sql)
    ret = cursor.fetchmany(3)
    print(ret)
    return json.dumps(ret)

@app.route('/api/categorys')
def category():
    result = Category.query.all()
    print(result)
    return 'aaa'

if __name__ == '__main__':
    app.run(debug=True)