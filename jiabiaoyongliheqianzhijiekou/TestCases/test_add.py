"""
======================
Author: 柠檬班-小简
Time: 2020/7/20 20:20
Project: jiabiaoyongliheqianzhijiekou
Company: 湖南零檬信息技术有限公司
======================
"""
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

# 读数据
he = HandleExcel(datas_dir + "\\api_cases.xlsx", "加标")
cases = he.read_all_datas()
he.close_file()
#以上三行放外面相当于全部都适用，相当于全局变量。放到class里面的话只能适用于类里面
db = HandleDB()
@ddt
class TestAdd(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        logger.info("************** 加标接口 开始测试 ************")
        # 清理 EnvData里设置的属性，保证加标接口使用环境变量类的时候，没有任何的动态属性。由我自己添加
        clear_EnvData_attrs()
        # 调用登陆接口，得到token和member_id

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("************** 加标接口 结束测试 ************")

    @data(*cases)#只能放到前面，放到函数里面就不认识了
    def test_add(self,case):
        # 替换case -
        case = replace_case_by_regular(case)
        # 如果前置sql - 得到结果后，再次替换。这里把前置直接写到excel里了(excel里的before),而且表中extract_data要传参
        # 发送请求 - 考虑用例是否都需要token
        if hasattr(EnvData,"admin_token"):
            response = send_requests(case["method"],case["url"],case["request_data"],token=EnvData.admin_token)
        else:
            response = send_requests(case["method"], case["url"], case["request_data"])#如果没有token,则直接发送请求
        #expected = eval(case["expected"])
        # 如果有提取表达式，提取数据，设置为全局变量。
        if case["extract_data"]:
            extract_data_from_response(case["extract_data"],response.json())
        # # 如果有期望结果，则断言
        # try:
        #     self.assertEqual(response.json()["code"], expected["code"])
        #     self.assertEqual(response.json()["msg"], expected["msg"])
        #  #如果有check_sql,数据库较验。
        #     # if case["check_sql"]:
        #     #      # logger.info()
        #     #      result = db.select_one_data(case["check_sql"])
        #     #      self.assertIsNotNone(result)
        # except AssertionError:
        #          logger.exception("断言失败！")
        #          raise


