# -*- coding:utf-8 -*-
__author__ = "leo"

import mock
import requests
import unittest


url = "http://www.imooc.com/login/register"

data = {
    "username": "user111",
    "password": "123qwe"
}


def post_request(url, data):
    res = requests.post(url, data=data).json()
    return res


def get_request(url, data):
    res = requests.get(url, params=data).json()
    return res


class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        print("case 开始执行")

    def tearDown(self) -> None:
        print("case 执行结束")

    def test_01(self):
        url = "http://www.imooc.com/login/register"

        data = {
            "username": "user111",
            "password": "123qwe"
        }

        success_test = mock.Mock(return_value=data)
        post_request = success_test
        res = post_request
        self.assertEqual("123qw", res())


if __name__ == '__main__':
    unittest.main()