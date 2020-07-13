#-*-coding:utf-8-*-
import HTMLTestRunner
import unittest
from time import strftime, localtime, time
from testcase import denglu
from testcase.denglu import login

suite = unittest.TestSuite()
# 获取TestSuite的实例对象
suite.addTest(denglu.login("test_1"))
# 把测试用例添加到测试容器中

now = strftime("%Y-%m-%d %H_%M_%S", localtime(time()))
# 获取当前时间
filename ="C:\\Users\\wyd\\workspace\\后台管理系统自动化测试\\" +now + "-AutomatedTestReport.html"
# 文件名

fp = open(filename, "wb+")
# 以二进制的方式打开文件并写入结果
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    verbosity=2,
    title="登录测试",
    description="测试详情")

runner.run(suite)
fp.close()