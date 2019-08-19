from flask import Flask, jsonify, request
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

# 定义路由
@app.route('/routine/get_routine_style', methods=['GET', 'POST'])
def get_routine_style():
    #return json.dumps({'code': 200, 'msg': "ok", "data": {"routine_style": "#000000"}})
    # 设置小程序导航栏 样式
    result['data'] = {"routine_style": "#000000"}
    return jsonify(result)

# 站点信息（logo和name）接口
@app.route('/routine/get_site_info', methods=['POST'])
def get_site_info():
    result['data'] = {"logo": "", 'name': '冬冬的商城'}
    return jsonify(result)

# 登录接口
@app.route('/routine/login', methods=['POST'])
def login():
    """
    通过前端传递的code获取openid 然后查询该openid是否已经在数据库表 中存在。
    如果不存在，在把前端传递过的 用户昵称 头像 性别 城市 openid 以新用户的方式
    注册到用户表中。
    :return:
    """
    # print(request.form.get('code', ''))
    # 获取数据转换成json
    # print(request.form)
    # code = request.form.get('code')
    # print(code)
    print(type(request.json), request.json, request.json['info']['code'])
    # code 前端传递的code  获取当前用户的 标识 openid
    code = request.json['info']['code']
    res = requests.get(url="https://api.weixin.qq.com/sns/jscode2session?appid=wx3660c66d7d17910a&secret=e497a74fc8e16addd9b3d50e458c3c99&js_code=%s&grant_type=authorization_code" % (code,))
    print(res.text)

    result['data'] = {"uid": 1}
    return jsonify(result)

# 小程序首页接口
@app.route('/routine/index', methods=['POST'])
def index():
    uid = request.args.get('uid', None)
    if not uid:
        result['code'] = '10001' # 规定是没有传递uid 验证参数
        result['msg'] = '请先登录后在访问首页！'
        return jsonify(result)

    result['data'] = {
        'banner': [
            {'url': 'http://www.baidu.com', 'pic': '/images/banner.jpg'},
            {'url': 'http://www.baidu.com', 'pic': '/images/banner.jpg'},
            {'url': 'http://www.baidu.com', 'pic': '/images/banner.jpg'}
        ]
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run()
