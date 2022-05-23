"""
======================
Author: 柠檬班-小简
Time: 2020/7/17 20:18
Project: day9
Company: 湖南零檬信息技术有限公司
======================
"""
#提现借口
# @ddt
# class TestRecharge(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls) -> None:
#         # 得到登陆的用户名和密码
#         user,passwd = get_old_phone()
#         # 登陆接口调用。
#         resp = send_requests("POST","member/login",{"mobile_phone":user,"pwd":passwd})
#         # cls.member_id = jsonpath(resp.json(),"$..id")[0]
#         # cls.token = jsonpath(resp.json(),"$..token")[0]
#         setattr(EnvData,"member_id",str(jsonpath(resp.json(),"$..id")[0]))
#         setattr(EnvData, "token", jsonpath(resp.json(),"$..token")[0])
