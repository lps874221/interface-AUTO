import unittest
from HTMLTestRunnerNew import HTMLTestRunner
from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.handle_path import cases_dir,reports_dir
#实例化套件对象
s = unittest.TestSuite()
#TestLoader的用法
#1、实例化TestLoader对象
# 2、使用discover去找到一个目录下的所有测试用例
#3、使用s
loader = unittest.TestLoader()
s.addTests(loader.discover(cases_dir))#不光是同级目录，里面子目录的用例也可以收集到
# #运行
# runner = unittest.TextTestRunner()
# runner.run(s)

fp = open(reports_dir + '/autoTest_report.html', 'wb')
runner = HTMLTestRunner(
            stream=fp,
            title='单元测试报告',
            description='单元测试报告',
            tester="小简"
            )
runner.run(s)