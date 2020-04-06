# -*- coding:utf-8 -*-
__author__ = "leo"

import requests
import unittest

from base.base_request import b_request

url = "http://www.imooc.com"
data = {
    "username": "123qwe",
    "password": "123qweasd"
}


class TestCase01(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("class ============")

    @classmethod
    def tearDownClass(cls) -> None:
        print("end ===========")

    def setUp(self) -> None:
        print("case 开始执行")

    def tearDown(self) -> None:
        print("case 结束执行")

    @unittest.skip("0007  无需执行")
    def test_07(self):
        print("case 0007 开始执行")

    def test_01(self):
        print("case 0001 开始执行")
        # res = requests.get(url=url, params=data).json()
        data1 = {
            "username": "wer"
        }
        self.assertDictEqual(data1, data)

    def test_02(self):
        print("case 0002 开始执行")
        data1 = {
            "username": "123qwe",
            "password": "123qweasd"
        }
        self.assertDictEqual(data1, data)

    @unittest.skip("0003 无需执行")
    def test_03(self):
        print("case 0003 开始执行")
        flag = True
        self.assertFalse(flag)

    def test_04(self):
        print("case 0004 开始执行")
        flag = False
        self.assertFalse(flag)

    @unittest.skip("0005 无需执行")
    def test_05(self):
        print("case 0005 开始执行")
        flag = 111
        flag1 = 222
        self.assertEqual(flag, flag1)

    def test_06(self):
        res = b_request.run_main("get", url, data)
        print(res)


if __name__ == '__main__':

    # unittest.main()
    suite = unittest.TestSuite()
    # suite.addTest(TestCase("test_07"))
    # suite.addTest(TestCase("test_03"))
    # suite.addTest(TestCase("test_05"))
    tests = [TestCase01("test_06"), TestCase01("test_05"), TestCase01("test_03")]
    suite.addTests(tests)
    runner = unittest.TextTestRunner()
    runner.run(suite)