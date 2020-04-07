# -*- coding:utf-8 -*-
__author__ = "leo"

import os

import configparser

base_path = os.path.dirname(os.getcwd())


class HandleIni:
    def load_ini(self):
        file_path = base_path + "/config/server.ini"
        cf = configparser.ConfigParser()
        cf.read(file_path, encoding="utf-8-sig")
        return cf

    def get_value(self, key, node=None):
        if not node:
            node = "server"
        cf = self.load_ini()
        try:
            data = cf.get(node, key)
        except:
            print("没有获取到值")
            data = None
        return data


handle_ini = HandleIni()

# if __name__ == '__main__':
#     test = HandleIni()
#     print(test.get_value("password"))