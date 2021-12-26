from flask import jsonify, request
from .moudle import Liuhuimin_Woaini as LW
from liuhuimin_woaini import liuhuimin_woaini_blue

lhmwan= LW.LHMWAN()

@liuhuimin_woaini_blue.route('/wirte', methods=['POST'])
def api_write_text():
    request_data =  LW.api_write_text(lhmwan,request.json)
    return jsonify(request_data)

@liuhuimin_woaini_blue.route('/read', methods=['POST'])
def api_read_text():
    request_data =  LW.api_read_text(lhmwan,request.json)
    return jsonify(request_data)
