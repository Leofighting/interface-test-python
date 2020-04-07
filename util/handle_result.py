# -*- coding:utf-8 -*-
__author__ = "leo"

from util.handle_json import handle_json
from deepdiff import DeepDiff

res = handle_json.get_value("api3/getbanneradvertver2", "/config/code_message.json")


# print(res)


def handle_result(url, code):
    data = handle_json.get_value(url, "/config/code_message.json")
    if data:
        for every_data in data:
            message = every_data.get(code)
            if message:
                return message
    return None


def handle_result_json(dict1, dict2):
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        cmp_dict = DeepDiff(dict1, dict2, ignore_order=True).to_dict()
        if cmp_dict.get("dictionary_item_added"):
            return False
        else:
            return True

    return False


def get_result_json(url, status):
    data = handle_json.get_value(url, "/config/result.json")
    if data:
        for every_data in data:
            message = every_data.get(status)
            if message:
                return message
    return None


if __name__ == '__main__':
    message = handle_result("api3/getbanneradvertver2", "10002")
    print(message)
