

# @ddt
# class TestRecharge(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls) -> None:
#         user,passwd = get_old_phone()
#         resp = send_requests("POST","member/login",{"mobile_phone":user,"pwd":passwd})
#         # cls.member_id = jsonpath(resp.json(),"$..id")[0]
#         # cls.token = jsonpath(resp.json(),"$..token")[0]
#         setattr(EnvData,"member_id",str(jsonpath(resp.json(),"$..id")[0]))
#         setattr(EnvData, "token", jsonpath(resp.json(),"$..token")[0])
