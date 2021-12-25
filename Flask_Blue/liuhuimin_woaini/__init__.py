#不要格式化文档，会报错
from flask import Blueprint
liuhuimin_woaini_blue = Blueprint('liuhuimin_woaini', __name__, url_prefix='/liuhuimin_woaini',
                       static_folder='static', template_folder="templates")
from . import route
