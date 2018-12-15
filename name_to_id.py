import json
import time


class DataHandler:

    def __init__(self):
        try:
            with open('./image_data.json') as file:
                self.dict = json.load(file)
        except IOError:
            pass

    dict = {}

    def put_name(self, name):
        self.dict[name] = int(time.time())

    def get_id_by_name(self, name):
        return self.dict[name]

    def get_name_by_id(self, id):
        for name, uid in self.dict.items():
            if uid == id:
                return name

    def to_json(self):
        json_data = json.dumps(self.dict, ensure_ascii=False)
        f1 = open('./image_data.json', 'w+')
        f1.write(json_data)
        f1.close()
