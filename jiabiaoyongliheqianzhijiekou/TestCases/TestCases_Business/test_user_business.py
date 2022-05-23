"""
======================
Author: 柠檬班-小简
Time: 2020/7/17 20:31
Project: day9
Company: 湖南零檬信息技术有限公司
======================
"""
"""
从响应结果当中提取需要的值
#主流程跑一遍,但是不用细到所有单接口都跑到
注册  用户名和密码
登陆  同一用户名和密码
充值  上一个登陆接口返回值里的 token，member_id
提现  登陆接口返回值里的 token，member_id
加标  
"""
import unittest
from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.handle_phone import get_new_phone
from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.handle_data import EnvData,replace_case_by_regular,clear_EnvData_attrs
from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.myddt import ddt,data
from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.my_logger import logger
from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.handle_excel import HandleExcel
from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.handle_path import datas_dir
from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.handle_requests import send_requests
from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.handle_extract_data_from_response import extract_data_from_response


he = HandleExcel(datas_dir+"\\api_cases.xlsx","业务流")
cases = he.read_all_datas()
he.close_file()

@ddt
class TestUserBusiness(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # 清理环境变量EnvData
        clear_EnvData_attrs()

        # 生成一个新的手机号码。设置为全局变量。
        new_phone = get_new_phone()
        setattr(EnvData,"phone",new_phone)

    @data(*cases)
    def test_user_business(self,case):
        # 替换数据
        replace_case_by_regular(case)

        # 发起请求,判断是否需要传递token
        if hasattr(EnvData,"token"):
            response = send_requests(case["method"],case["url"],case["request_data"],token=EnvData.token)
        else:
            response = send_requests(case["method"], case["url"], case["request_data"])

        # 如果有要提取数据的，提取数据。并设置为全局变量。
        if case["extract_data"]:
            extract_data_from_response(case["extract_data"],response.json())

