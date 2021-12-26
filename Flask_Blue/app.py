
from liuhuimin_woaini import liuhuimin_woaini_blue
from flask import Flask, Blueprint
from flask_cors import CORS
app = Flask(__name__)
app.register_blueprint(liuhuimin_woaini_blue)
CORS(app, supports_credentials=True)
if __name__ == '__main__':
    # 这里的代码如果使用uwsgi运行的话是不会被执行的哦~
    # 所以一定不要单独用flas-run做生产环境哦~
    # 下面的语句，为方便调试，开启了允许全局跨域，开启了debug模式，都很危险哦~
    # from flask_cors import CORS
    # CORS(app, supports_credentials=True)
    app.run(host='0.0.0.0', port='5000', debug=True)
