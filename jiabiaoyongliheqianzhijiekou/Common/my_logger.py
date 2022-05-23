

import logging
import os

from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.handle_config import conf
from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.handle_path import logs_dir

class MyLogger(logging.Logger):

    def __init__(self,file=None):
        # super().__init__(name,level)
        super().__init__(conf.get("log","name"),conf.get("log","level"))

       
        fmt = '%(asctime)s %(name)s %(levelname)s %(filename)s-%(lineno)d line：%(message)s'
        formatter = logging.Formatter(fmt)

      
        handle1 = logging.StreamHandler()
        handle1.setFormatter(formatter)
        self.addHandler(handle1)

        if file:
            handle2 = logging.FileHandler(file,encoding="utf-8")
            handle2.setFormatter(formatter)
            self.addHandler(handle2)


if conf.getboolean("log","file_ok"):
    file_name = os.path.join(logs_dir,conf.get("log","file_name"))
else:
    file_name = None


logger = MyLogger(file_name)

# logger.info("1111111111111111")
