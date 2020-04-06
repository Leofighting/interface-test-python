# -*- coding:utf-8 -*-
__author__ = "leo"

import requests
import json

res = requests.get("https://m.imooc.com/api/search/searchword", verify=False)
print(res)