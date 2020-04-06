# -*- coding:utf-8 -*-
__author__ = "leo"

import requests
import json

# url = "https://www.imooc.com/user/postpic"
download_url = "http://file.mukewang.com/apk/app/114/imooc7.3.310102001android.apk?version=1584346839"
file = {
    "fileField": ("雪鸮鸟.jpg", open("C:/Users/xiaoj/Pictures/Saved Pictures/雪鸮鸟.jpg", "rb"), "image/jpeg"),
    "type": "1"
}

cookie = {
    "apsid": "hhNmI2N2NkNDE4YTdkMGNmNjQyYzkxNTdjMmFjMWIAAAAAAAAAA"
}

# res = requests.post(url, files=file, cookies=cookie, verify=False).json()

res = requests.get(download_url)
with open("mukewang.apk", "wb") as f:
    f.write(res.content)
