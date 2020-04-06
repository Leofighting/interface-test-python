# -*- coding:utf-8 -*-
__author__ = "leo"

import unittest
import json
import os

import mock
import HTMLTestRunner_PY3

from base.base_request import b_request

host = "https://www.imooc.com/"
base_path = os.path.dirname(os.getcwd())


def read_json():
    with open(base_path + "/config/user_data.json") as f:
        data = json.load(f)
    return data


def get_value(key):
    data = read_json()
    return data[key]


class ImoocCase(unittest.TestCase):
    def test_banner(self):
        url = host + 'api3/getbanneradvertver2'
        data = {
            'timestamp': '1561269343481',
            'uid': '7213561',
            'token': '7ad09430cbaf927af642ab843ec374ef',
            'type': '1',
            'marking': 'androidbanner',
            'uuid': '41b650ef846688193728ff7381eb6c1c',
            'secrect': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWUiOiI3MjEzNTYxIiwianRpIjoiM2I2NDg0NjQ2Nzk4NjI3NzU1YjRmZWE0ODliMDNmNmUiLCJkZXZpY2UiOiJtb2JpbGUifQ.EvGIFSHhij4lgEMdCtotFoTMtWSJLwVvridsoaWzdZY'
        }
        mock_method = mock.Mock(return_value=get_value("/api3/getbanneradvertver2"))
        b_request.run_main = mock_method
        res = b_request.run_main("post", url, data)
        self.assertEqual(res["errorCode"], 1001)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ImoocCase("test_banner"))
    file_path = base_path + "/report/report01.html"
    with open(file_path, 'wb') as f:
        runner = HTMLTestRunner_PY3.HTMLTestRunner(stream=f, title="this is test", description="Leo test")
        runner.run(suite)
    # f.close()
    # unittest.main()
