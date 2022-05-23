
import jsonpath
from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.handle_data import EnvData
from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.my_logger import logger


def extract_data_from_response(extract_exprs,response_dict):
    extract_dict = eval(extract_exprs)
    logger.info("要从响应结果当中提取的数据集为：\n{}".format(extract_dict))
    for key,value in extract_dict.items():
        res = str(jsonpath.jsonpath(response_dict,value)[0])
                                       
        logger.info("设置环境变量.key:{},value:{}".format(key,res))
        setattr(EnvData,key,res)


if __name__ == '__main__':
     ss = '{"member_id":"$..id","token":"$..token"}'
     response = {'code': 0, 'msg': 'OK',
                 'data': {'id': 200713, 'leave_amount': 8555405.44, 'mobile_phone': '18605671115',
                          'reg_name': '美丽可爱的小简', 'reg_time': '2020-06-29 11:52:20.0', 'type': 1,
                          'token_info': {'token_type': 'Bearer', 'expires_in': '2020-07-08 21:33:05',
                                         'token': 'eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjIwMDcxMywiZXhwIjoxNTk0MjE1MTg1fQ.9oTx_KSOwjEg4V9Ez_P6QV-3aBk3QCCFRZk3OlTnGDElkVanMLFK_H5wgI_9xolnjBNZE9TMI7e1nSOPKWj2HA'}}}

     extract_data_from_response(ss,response)
     print(EnvData.__dict__)
