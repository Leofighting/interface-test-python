# -*- coding:utf-8 -*-
__author__ = "leo"

import json

import requests


class BaseRequest:

    def send_post(self, url, data):
        res = requests.post(url=url, data=data, verify=False).text
        return res

    def send_get(self, url, data):
        res = requests.get(url=url, params=data, verify=False).text
        return res

    def run_main(self, method, url, data):
        if method == "get":
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)

        try:
            res = json.loads(res)
        except:
            print("结果是一个 text")
        return res


b_request = BaseRequest()