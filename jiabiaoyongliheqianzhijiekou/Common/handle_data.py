
import re
from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.handle_config import conf
import json
from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.my_logger import logger



class EnvData:
    
    pass

def clear_EnvData_attrs():
    values = dict(EnvData.__dict__.items())
    for key, value in values.items():
        if key.startswith("__"):
            pass
        else:
            delattr(EnvData, key)


def replace_case_by_regular(case):
    for key,value in case.items():
        if value is not None and isinstance(value, str):  # 确保是个字符串
            case[key] = replace_by_regular(value)
    logger.info("正则表达式替换完成之后的请求数据：\n{}".format(case))
    return case

def replace_by_regular(data):
    res = re.findall("#(.*?)#", data)  
    if res:
        for item in res:
            try:
                value = conf.get("data", item)
            except:
                try:
                    value = getattr(EnvData, item)
                except AttributeError:
                    # value = "#{}#".format(item)
                    continue
            print(value)
            data = data.replace("#{}#".format(item), value)
    return data


def replace_mark_with_data(case,mark,real_data):
    for key,value in case.items():
        if value is not None and isinstance(value,str): 
            if value.find(mark) != -1: 
                case[key] = value.replace(mark,real_data)
    return case

if __name__ == '__main__':
    case = {
        "method": "POST",
        "url": "http://api.lemonban.com/futureloan/#phone#/member/register",
        "request_data": '{"mobile_phone": "#phone#", "pwd": "123456789", "type": 1, "reg_name": "美丽可爱的小简"}'
    }
    if case["request_data"].find("#phone#") != -1:
        case = replace_mark_with_data(case, "#phone#", "123456789006")#这里用123456789001看看可否成功替换
    for key,value in case.items():
        print(key,value)
