# -*- coding:utf-8 -*-
__author__ = "leo"

import json
import os

import unittest

from base.base_request import b_request
from util.handle_excel import excel_data
from util.handle_result import handle_result, handle_result_json, get_result_json

base_path = os.path.dirname(os.getcwd())


class RunMain:
    def run_case(self, index=None):
        rows = excel_data.get_rows(index)
        for i in range(2, rows + 1):
            data = excel_data.get_row_value(i)
            is_run = data[2]

            if is_run == "yes":
                method = data[5]
                url = data[4]
                data1 = data[6]
                expect_method = data[8]
                expect_result = data[9]
                res = b_request.run_main(method=method, url=url, data=data1)
                code = str(res["errorCode"])
                message = res["errorDesc"]

                if expect_method == "mec":
                    config_message = handle_result(url, code)
                    if message == config_message:
                        excel_data.excel_write_data(i, 11, "通过")
                    else:
                        excel_data.excel_write_data(i, 11, "失败")
                        excel_data.excel_write_data(i, 12, json.dumps(res))

                if expect_method == "errorcode":
                    if expect_result == code:
                        excel_data.excel_write_data(i, 11, "通过")
                    else:
                        excel_data.excel_write_data(i, 11, "失败")
                        excel_data.excel_write_data(i, 12, json.dumps(res))

                if expect_method == "json":
                    if code == "1000":
                        status_str = "success"
                    else:
                        status_str = "error"
                    expect_result = get_result_json(url, status_str)
                    result = handle_result_json(res, expect_result)
                    if result:
                        excel_data.excel_write_data(i, 11, "通过")
                    else:
                        excel_data.excel_write_data(i, 11, "失败")
                        excel_data.excel_write_data(i, 12, json.dumps(res))


if __name__ == '__main__':
    run_main = RunMain()
    run_main.run_case()
