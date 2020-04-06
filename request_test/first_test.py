# -*- coding:utf-8 -*-
__author__ = "leo"

import json

import requests

url = "https://www.imooc.com/search/hotwords"
get_url = "https://www.imooc.com/common/adver-getadver"

res_test = requests.get(get_url, verify=False).json()
print(json.dumps(res_test, indent=4, ensure_ascii=False))