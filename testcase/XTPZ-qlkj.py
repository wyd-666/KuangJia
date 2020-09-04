from selenium import webdriver
import unittest
from time import sleep
from time import sleep
from public.Login import Deng_lu
from selenium.webdriver.support.select import Select

class XTPZ(unittest.TestCase):
    dr = webdriver.Chrome()
    def setUp(self):
        self.dr.get('http://192.168.0.205/admin')
    def test_qlkj(self):
        deng_lu = Deng_lu(self.dr)
        deng_lu.denglu()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[7]/span').click()
        self.dr.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[7]/div/div[3]').click()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/table/tbody/tr[2]/td/form/span[2]/input[1]').clear()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/table/tbody/tr[2]/td/form/span[2]/input[1]').send_keys('180')
        self.dr.find_element_by_id('startTime').click()
        #self.dr.find_element_by_id('startTime').send_keys('2020-01-01')
        self.dr.find_element_by_xpath('//*[@id="layui-laydate1"]/div[1]/div[1]/i[2]').click()
        self.dr.find_element_by_xpath('//*[@id="layui-laydate1"]/div[1]/div[1]/i[2]').click()
        self.dr.find_element_by_xpath('//*[@id="layui-laydate1"]/div[1]/div[1]/i[2]').click()
        self.dr.find_element_by_xpath('//*[@id="layui-laydate1"]/div[1]/div[1]/i[2]').click()
        self.dr.find_element_by_xpath('//*[@id="layui-laydate1"]/div[1]/div[1]/i[2]').click()
        self.dr.find_element_by_xpath('//*[@id="layui-laydate1"]/div[1]/div[1]/i[2]').click()
        self.dr.find_element_by_xpath('//*[@id="layui-laydate1"]/div[1]/div[1]/i[2]').click()
        self.dr.find_element_by_xpath('//*[@id="layui-laydate1"]/div[1]/div[2]/table/tbody/tr[3]/td[4]').click()
        sleep(5)
        self.dr.find_element_by_id('endTime').click()
        self.dr.find_element_by_xpath('//*[@id="layui-laydate2"]/div[1]/div[1]/i[2]').click()
        self.dr.find_element_by_xpath('//*[@id="layui-laydate2"]/div[1]/div[1]/i[2]').click()
        self.dr.find_element_by_xpath('//*[@id="layui-laydate2"]/div[1]/div[1]/i[2]').click()
        self.dr.find_element_by_xpath('//*[@id="layui-laydate2"]/div[1]/div[1]/i[2]').click()
        self.dr.find_element_by_xpath('//*[@id="layui-laydate2"]/div[1]/div[1]/i[2]').click()
        self.dr.find_element_by_xpath('//*[@id="layui-laydate2"]/div[1]/div[1]/i[2]').click()
        self.dr.find_element_by_xpath('//*[@id="layui-laydate2"]/div[1]/div[2]/table/tbody/tr[2]/td[3]').click()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/table/tbody/tr[3]/td/button').click()
        self.dr.find_element_by_class_name('layui-layer-btn1').click()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/table/tbody/tr[4]/td/form/span[2]/div/em').click()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/table/tbody/tr[4]/td/form/span[2]/div/em').click()
        sleep(4)








    def tearDown(self):
        self.dr.close()


if __name__ == '__main__':
        unittest.main()