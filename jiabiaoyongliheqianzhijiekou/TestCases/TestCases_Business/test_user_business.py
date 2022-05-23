
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
        clear_EnvData_attrs()
        new_phone = get_new_phone()
        setattr(EnvData,"phone",new_phone)

    @data(*cases)
    def test_user_business(self,case):
        replace_case_by_regular(case)
        if hasattr(EnvData,"token"):
            response = send_requests(case["method"],case["url"],case["request_data"],token=EnvData.token)
        else:
            response = send_requests(case["method"], case["url"], case["request_data"])
        if case["extract_data"]:
            extract_data_from_response(case["extract_data"],response.json())

