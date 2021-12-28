from flask import jsonify, request
from .moudle import Nebula_BH_No_1 as LW
from flask import Blueprint



# 定义蓝图，初始化蓝图对象
Nebula_BH_No_1_blue = Blueprint('Nebula_BH_No_1', __name__, url_prefix='/Nebula_BH_No_1')
lhmwan = LW.LHMWAN(Nebula_BH_No_1_blue)
@Nebula_BH_No_1_blue.route('/wirte', methods=['POST'])
def api_write_text():
    return jsonify(LW.api_write_text(lhmwan, request.json))


@Nebula_BH_No_1_blue.route('/read', methods=['POST'])
def api_read_text():
    return jsonify(LW.api_read_text(lhmwan, request.json))
