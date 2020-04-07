# -*- coding:utf-8 -*-
__author__ = "leo"

import os
import json

base_path = os.path.dirname(os.getcwd())


class HandleJson:
    def read_json(self, file_name=None):
        if not file_name:
            file_path = base_path + "/config/user_data.json"
        else:
            file_path = base_path + file_name
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        return data

    def get_value(self, key, file_name=None):
        data = self.read_json(file_name)
        return data.get(key)


handle_json = HandleJson()
