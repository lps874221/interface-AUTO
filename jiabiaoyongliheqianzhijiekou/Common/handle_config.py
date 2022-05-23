
from configparser import ConfigParser
import os

from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.handle_path import conf_dir

class HandleConfig(ConfigParser):

    def __init__(self,file_path):
        super().__init__()
        self.read(file_path, encoding="utf-8")



file_path = os.path.join(conf_dir, "nmb.ini")
conf = HandleConfig(file_path)


# if __name__ == '__main__':
#     conf = HandleConfig("nmb.ini")
#     conf.get("log","name")
