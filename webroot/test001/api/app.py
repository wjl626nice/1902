from flask import Flask
#导入模块
from flask_sqlalchemy import SQLAlchemy
import pymysql

#创建flask对象
app = Flask(__name__)

#配置flask配置对象中键：SQLALCHEMY_DATABASE_URI

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@127.0.0.1/myblog"

#配置flask配置对象中键：SQLALCHEMY_COMMIT_TEARDOWN,设置为True,应用会自动在每次请求结束后提交数据库中变动

app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

#获取SQLAlchemy实例对象，接下来就可以使用对象调用数据

db = SQLAlchemy(app)