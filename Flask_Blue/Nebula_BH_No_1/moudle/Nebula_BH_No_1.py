import random
import json
import time
from py2neo import Graph, NodeMatcher, Node, Relationship
from py2neo.matching import *
import hashlib
import yaml
from urllib.parse import urljoin
from .public import get_service_time
import os


class LHMWAN():
    # 保留蓝图内的所有相关信息，供调用，不提供方法
    blue_info = ''
    config = ''
    path = ''
    graph = ''

    def __init__(self, blue_info):
        """初始化数据"""
        # 取得蓝图基本信息，保留蓝图对象
        self.blue_info = blue_info
        # 蓝图路径
        self.path = blue_info.root_path
        # 读取配置文件
        with open(os.path.join(self.path, "config/config.yaml"), 'r',encoding='utf-8') as f:
            config = yaml.safe_load(f)
        self.config = config
        
        # 与neo4j服务器建立连接,取的服务器图形对象。
        try:
            neo4j_config = config['database']['neo4j']
            self.graph = Graph(**neo4j_config)
        except Exception as e:
            print("数据库加载错误")
            exit()


def write_one_mail(graph, mail_text):
    # 接受mail内容，写入成功返回0
    response = {
        "code": 0,
        'msg': ''
    }
    hl = hashlib.md5()
    hl.update(mail_text.encode(encoding='utf-8'))
    mail_text_hash = hl.hexdigest()
    node_properties = {
        'Flag': 'Nebula.BH.No.1',
        "mail_text": mail_text,
        "time": get_service_time(),
        "IP": "",
        "mail_ID": "",  # 考虑随机数加时间进行标号，因为时间因数，不会有重复值的。
        "hash": mail_text_hash  # 用来记录text 的hash，如果有重复，那么禁止提交
    }
    nodes = NodeMatcher(graph)
    result = len(nodes.match("Nebula.BH.No.1", Flag='Nebula.BH.No.1', hash=mail_text_hash)
                 )
    if not result == 0:
        response['code'] = 1
        response['msg'] = "哦！天呐！怎么可能会有两个人给我发同样的信件啊！"
    try:
        # 建立节点对象
        node = Node("Nebula.BH.No.1", **node_properties)
        graph.create(node)
    except Exception as e:
        response['code'] = 1
        response['msg'] = "发送失败 失败代码：173420897682453987"
        return response
    return response


def read_one_mail(graph, readed_list):
    # 接受已读信件的hash列表
    # 返回不在hash列表内的信件内容
    # 从数据库中直接查询一条记录就行了，不需要队列
    response = {
        'code': 0,
        'msg': '',
        'mailID': ''
    }
    nodes = NodeMatcher(graph)
    result = nodes.match("Nebula.BH.No.1", Flag='Nebula.BH.No.1')
    for i in iter(result):
        if i['hash'] not in readed_list and i['hash'] != 'Null':
            response['msg'] = i["mail_text"]
            response['mailID'] = i['hash']
            return response
            break
    response['msg'] = "小站的信件被读完了"
    return response


def api_write_text(LHMWAN, POST):
    write_text = POST['write_text']
    req = write_one_mail(LHMWAN.graph, write_text)
    return req


def api_read_text(LHMWAN, POST):
    root_path = LHMWAN.path
    file_path = LHMWAN.config['others']['file_path']
    req = {"code": 0,
           "msg": ''}
    if POST['action'] == 'read_mail':
        readed_list = POST['readed_list']
        req = read_one_mail(LHMWAN.graph, readed_list)
    elif POST['action'] == 'read_my_story':
        with open(os.path.join(root_path, file_path['Read_my_story_md']), 'r', encoding='utf-8') as f:
            req['msg'] = f.read()
    elif POST['action'] == 'read_Home':
        with open(os.path.join(root_path, file_path['Home_md']), 'r', encoding='utf-8') as f:
            req['msg'] = f.read()
    return req
