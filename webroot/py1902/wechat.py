import json, os
from flask import Flask,request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/wechat/')
def wechat():
    data = request.args
    # data = json.dumps(data)
    # file_path = os.path.dirname(__file__)
    # with open(os.path.join(file_path, 'test.txt'), 'a+') as f:
    #     f.write(data)

    return data['echostr']

@app.route('/xuxin/')
def hello_xuxin():
    return 'Hello xuxin'

if __name__ == '__main__':
    app.run()