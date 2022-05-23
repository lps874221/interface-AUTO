"""
#
======================
Author: 柠檬班-小简
Time: 2020/7/6 21:13
Project: day6
Company: 湖南零檬信息技术有限公司
======================
"""
"""
充值接口：
   所有用例的前置：登陆！
                拿到2个数据：id，token
   把前置的数据，传递给到测试用例。
   
   充值接口的请求数据：id
             请求头：token
             
遇到的问题一：充值前的用户余额：{'leave_amount': Decimal('4536202.88')}
    处理sql语句：把Decimal对应的字段值修改为字符串返回。CAST(字段名 AS CHAR)
    select CAST(member.leave_amount AS CHAR) as leave_amount from member where id=#member_id#;
    方式二：Decimal类
    
优化方式：
"""

import unittest
from jsonpath import jsonpath

from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.handle_phone import get_old_phone
import os
import json

from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.handle_requests import send_requests
from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.handle_excel import HandleExcel
from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.myddt import ddt,data
from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.handle_path import datas_dir
from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.my_logger import logger
from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.handle_db import HandleDB
from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.handle_data import replace_case_by_regular,EnvData,clear_EnvData_attrs


he = HandleExcel(datas_dir+"\\api_cases.xlsx","充值")
cases = he.read_all_datas()
he.close_file()

db = HandleDB()

@ddt
class TestRecharge(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # 清理 EnvData里设置的属性
        clear_EnvData_attrs()

        # 得到登陆的用户名和密码
        user,passwd = get_old_phone()
        # 登陆接口调用。
        resp = send_requests("POST","member/login",{"mobile_phone":user,"pwd":passwd})
        #   = jsonpath(resp.json(),"$..id")[0]
        # cls.token = jsonpath(resp.json(),"$..token")[0]
        setattr(EnvData,"member_id",str(jsonpath(resp.json(),"$..id")[0]))#$后面点点的意思是在resp.json下面让它自己找id，因为这里是个列表，我们希望取到的是值，所以取第一个[0]（可能ID不止一个，所以要用数字顺序来注明）
                                                                          #一般jsonpath取值返回的都是列表形式
        setattr(EnvData, "token", jsonpath(resp.json(),"$..token")[0])#这里的member_id和token就是类属性
        #和上一个接口设置直接设置全局变量传递到下一个接口不同的是，这里是设置一个类变量来传递，然后通过类属性来访问
        #和上面注释掉的cls.member_id...是两个方法，二选一都可以，但是cls不能全面支持业务流，setattr方法可以全面支持比较方便

    # def tearDown(self) -> None:
    #     if hasattr(EnvData,"money"):#因为在上一条用例传给下一条用例的money值后，就没有带#号的money继续传递，已经存在值不对了。所以要在本条用例结束之后或下一条用例开始之前就将money环境变量删除，这样不会影响下一次的替换
    #         delattr(EnvData,"money")#至于member_id与token为什么不删，因为用的是用一个账户，而不是两个账户。member_id都用的同一个没必要修改


    @data(*cases)
    def test_recharge(self,case):
        # 替换的数据
        if case["request_data"].find("#member_id#") != -1:
            case = replace_case_by_regular(case)

        # 数据库 - 查询当前用户的余额 - 在充值之前
        if case["check_sql"]:
            user_money_before_recharge = db.select_one_data(case["check_sql"])["leave_amount"]#
            logger.info("充值前的用户余额：{}".format(user_money_before_recharge))
            # 期望的用户余额。 充值之前的余额 + 充值的钱
            recharge_money = json.loads(case["request_data"])["amount"]#取excel表里的amount值
            logger.info("充值的金额为：{}".format(recharge_money))
            expected_user_leave_amount = round(float(user_money_before_recharge) + recharge_money,2)#leave_amount为小数点后两位，所以需要使用float，round是控制小数点位数的，2代表2位小数。四舍五入，详细见"扩展学习”中的“关于float..."一节
            logger.info("期望的充值之后的金额为：{}".format(expected_user_leave_amount))
            setattr(EnvData,"money",str(expected_user_leave_amount))#所有的环境变量全部设置为 字符串，这个时候debug可以看到充值前后的期望值是多少
            # 更新期望的结果 - 将期望的用户余额更新到期望结果当中。(更新到excel第一条数据当中并同步发生变化，然后再传到下一个接口去再替换）
            case = replace_case_by_regular(case)#对应上面说的全部用例，多个用例一起替换较为方便

        # 发起请求 - 给用户充值
        response = send_requests(case["method"],case["url"],case["request_data"],token=EnvData.token)#发送请求一定要带token，这就是上一个接口的属性传递到下一个接口

        # 将期望的结果转成字典对象，再去比对
        expected = json.loads(case["expected"])

        # 断言
        try:
            self.assertEqual(response.json()["code"], expected["code"])
            self.assertEqual(response.json()["msg"], expected["msg"])
            if case["check_sql"]:
                self.assertEqual(response.json()["data"]["id"], expected["data"]["id"])
                self.assertEqual(response.json()["data"]["leave_amount"], expected["data"]["leave_amount"])
                # 数据库 - 查询当前用户的余额
                user_money_after_recharge = db.select_one_data(case["check_sql"])["leave_amount"]
                logger.info("充值后的用户余额：{}".format(user_money_after_recharge))
                self.assertEqual("{:.2f}".format(expected["data"]["leave_amount"]),"{:.2f}".format(float(user_money_after_recharge)))
        except:
            logger.exception("断言失败！")
            raise
