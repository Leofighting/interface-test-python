# -*- coding:utf-8 -*-
__author__ = "leo"

import json

import requests

from util.handle_cookie import write_cookie
from util.handle_ini import handle_ini
from util.handle_json import handle_json


class BaseRequest:

    def send_post(self, url, data, cookie=None, get_cookie=None):
        response = requests.post(url=url, data=data, verify=False, cookie=cookie)
        if get_cookie:
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value, get_cookie["is_cookie"])

        res = response.text
        return res

    def send_get(self, url, data, cookie=None, get_cookie=None):
        response = requests.get(url=url, params=data, verify=False, cookie=cookie)
        if get_cookie:
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value, get_cookie["is_cookie"])
        res = response.text
        return res

    def run_main(self, method, url, data, cookie=None, get_cookie=None):
        # return handle_json.get_value(url)
        base_url = handle_ini.get_value("host")
        if "http" not in url:
            url = base_url + url
        print(url)
        if method == "get":
            res = self.send_get(url, data, cookie, get_cookie)
        else:
            res = self.send_post(url, data, cookie, get_cookie)

        try:
            res = json.loads(res)
        except:
            print("结果是一个 text")
        return res


b_request = BaseRequest()

if __name__ == '__main__':
    b_request = BaseRequest()
    b_request.run_main("get", "login", '{"username": "user1111"}')
