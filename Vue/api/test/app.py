from flask import Flask, jsonify, request, make_response
from flask_cors import cross_origin
import time
import requests
import json
# 创建一个app应用对象
app = Flask(__name__)

# 定义要返回的数据格式
result = {'code': 200, 'msg': "ok", "data": {}}

# 默认get 请求
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/firstTest')
@cross_origin()   # 解决跨域
def first_test():
    return 'first_test'

@app.route('/firstTests')
def firstTests():
    res = make_response('1111')
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    res.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return res

@app.route('/firstTest1')
@cross_origin()   # 解决跨域
def firstTest1():
   return '1111'


@app.route('/firstTest2')
@cross_origin()   # 解决跨域
def firstTest2():
   time.sleep(2)
   return '2222'


@app.route('/firstTest3')
@cross_origin()   # 解决跨域
def firstTest3():
    return '3333'

# http://www.xuxin.com/api/getdata
# http://api.xuxin.com/getdata
@app.route('/api/getdata')
@cross_origin()   # 解决跨域
def getdata():
    return jsonify({"id": 1, "title": 'aaa'})

@app.route('/api/getdata2')
@cross_origin()   # 解决跨域
def getdata2():
    return jsonify({"id": 1, "title": 'bbb'})

@app.route('/api/getdata3')
@cross_origin()   # 解决跨域
def getdata3():
    return jsonify({"id": 1, "title": 'ccc'})

if __name__ == '__main__':
    app.run()
