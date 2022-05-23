

import unittest
import os
from BeautifulReport import BeautifulReport

from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.handle_path import cases_dir,reports_dir,debug_dir

# 收集用例

s = unittest.TestLoader().discover(debug_dir)

# 生成报告
br = BeautifulReport(s)
br.report("py30-注册用例自动化", "report_.html",reports_dir)
