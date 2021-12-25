import random
import json


class LHMWAN():
    ID_list = []
    def __init__(self):
        with open("./liuhuimin_woaini/text/list.json", "r", encoding='utf-8') as f:
            self.ID_list = json.load(f)

    def write_id_to_file(self):
        with open("./liuhuimin_woaini/text/list.json", "w", encoding='utf-8') as f:
            json.dump(self.ID_list, f)
        pass

    def add_ID_list(self, ID):
        self.ID_list.append(ID)

    def get_ID_list(self):
        return self.ID_list

    def get_ID_list_len(self):
        return len(self.ID_list)


def api_write_text(LHMWAN, POST):
    filename = get_one_ID()
    write_text = POST['write_text']
    with open("./liuhuimin_woaini/text/{}".format(filename), "w", encoding='utf-8') as f:
        f.write(write_text)
    LHMWAN.add_ID_list(filename)
    print(LHMWAN.get_ID_list())
    LHMWAN.write_id_to_file()
    return {"code": 0}


def api_read_text(LHMWAN, POST):
    # 初始req
    req = {"code": 0,
           "msg": ''}
    # 随机一个ID
    randomID = random.choice(LHMWAN.ID_list)
    # 依据ID，读出文档
    with open("./liuhuimin_woaini/text/{}".format(randomID), "r", encoding='utf-8') as f:
        req['msg'] = f.read()
    return req
def get_one_ID():
    timedata = time.localtime()
    random_text1 = ""
    random_text2 = ""
    for i in range(10):
        random_text1 = random_text1+str(random.randint(0, 9))
    for i in range(10):
        random_text2 = random_text2+str(random.randint(0, 9))
    ID = "{}{}{}{}{}{}{}".format(
        random_text1, timedata[0], timedata[1], timedata[2], timedata[3], timedata[4], random_text2)
    return ID
