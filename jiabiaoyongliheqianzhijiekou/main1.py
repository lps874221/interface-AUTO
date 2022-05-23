import unittest
from HTMLTestRunnerNew import HTMLTestRunner
from ningmengban2019.day10.jiabiaoyongliheqianzhijiekou.Common.handle_path import cases_dir,reports_dir

s = unittest.TestSuite()
loader = unittest.TestLoader()
s.addTests(loader.discover(cases_dir))
# runner = unittest.TextTestRunner()
# runner.run(s)

fp = open(reports_dir + '/autoTest_report.html', 'wb')
runner = HTMLTestRunner(
            stream=fp,
            title='单元测试报告',
            description='单元测试报告',
            tester="tester"
            )
runner.run(s)
