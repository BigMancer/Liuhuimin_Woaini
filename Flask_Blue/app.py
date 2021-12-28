from flask_cors import CORS
import traceback
try:
    from flask import Flask
    # 引入蓝图
    from Nebula_BH_No_1 import Nebula_BH_No_1_blue
    # from flask_limiter import Limiter
    # from flask_limiter.util import get_remote_address
    app = Flask(__name__)
except Exception as e :
    # 由于flask在包含错误时候，报错过于简单，无法排错，采用这种方法，可以获得更好的报错信息
    traceback.print_exc()  
    print(e)
    exit()


# 注册蓝图
app.register_blueprint(Nebula_BH_No_1_blue)

# CORS(app, supports_credentials=True)
if __name__ == '__main__':

    # 这里的代码如果使用uwsgi运行的话是不会被执行的哦~
    # 所以一定不要单独用flas-run做生产环境哦~
    # 下面的语句，为方便调试，开启了允许全局跨域，开启了debug模式，都很危险哦~
    from flask_cors import CORS
    CORS(app, supports_credentials=True)
    app.run(host='0.0.0.0', port='5000', debug=True)
