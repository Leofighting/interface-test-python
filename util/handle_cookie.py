# -*- coding:utf-8 -*-
__author__ = "leo"

import os

from util.handle_json import HandleJson

handle_json = HandleJson()
base_path = os.path.dirname(os.getcwd())


def get_cookie_value(cookie_key):
    data = handle_json.read_json(file_name="/config/cookie.json")
    return data[cookie_key]


def write_cookie(data_input, cookie_key):
    data = handle_json.read_json(file_name="/config/cookie.json")
    data[cookie_key] = data_input
    handle_json.write_value(data)


if __name__ == '__main__':
    get_cookie_value()

