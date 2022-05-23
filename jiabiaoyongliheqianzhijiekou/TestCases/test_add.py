
import unittest
from jsonpath import jsonpath

import os
import json

from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.handle_requests import send_requests
from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.handle_excel import HandleExcel
from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.myddt import ddt,data
from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.handle_path import datas_dir
from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.my_logger import logger
from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.handle_db import HandleDB
from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.handle_data import replace_case_by_regular,EnvData,clear_EnvData_attrs
from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.handle_extract_data_from_response import extract_data_from_response


he = HandleExcel(datas_dir + "\\api_cases.xlsx", "加标")
cases = he.read_all_datas()
he.close_file()
db = HandleDB()
@ddt
class TestAdd(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        logger.info("************** 加标接口 开始测试 ************")
        clear_EnvData_attrs()


    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("************** 加标接口 结束测试 ************")

    @data(*cases)
    def test_add(self,case):
        case = replace_case_by_regular(case)
        if hasattr(EnvData,"admin_token"):
            response = send_requests(case["method"],case["url"],case["request_data"],token=EnvData.admin_token)
        else:
            response = send_requests(case["method"], case["url"], case["request_data"])
        #expected = eval(case["expected"])
        if case["extract_data"]:
            extract_data_from_response(case["extract_data"],response.json())
        # 
        # try:
        #     self.assertEqual(response.json()["code"], expected["code"])
        #     self.assertEqual(response.json()["msg"], expected["msg"])
        # 
        #     # if case["check_sql"]:
        #     #      # logger.info()
        #     #      result = db.select_one_data(case["check_sql"])
        #     #      self.assertIsNotNone(result)
        # except AssertionError:
        #          logger.exception("断言失败！")
        #          raise


