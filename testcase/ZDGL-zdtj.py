from selenium import webdriver
import unittest
from time import sleep
from time import sleep
from public.Login import Deng_lu
from selenium.webdriver.support.select import Select

class YHGL(unittest.TestCase):
    dr = webdriver.Chrome()
    def setUp(self):
        self.dr.get('http://192.168.0.205/admin/detector-list')
    def test_zdtj(self):
        deng_lu = Deng_lu(self.dr)
        deng_lu.denglu()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[6]/span').click()
        self.dr.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[6]/div/div[1]').click()
        sleep(3)
        self.dr.find_element_by_id('begin1').click()
        self.dr.find_element_by_id('begin1').clear()
        self.dr.find_element_by_id('begin1').send_keys('2020-06-10 00:00:00')
        sleep(2)
        self.dr.find_element_by_xpath('//*[@id="stat-overview"]/div[1]/button[1]').click()
        self.dr.find_element_by_id('begin1').click()
        self.dr.find_element_by_class_name('laydate-btns-confirm').click()
        sleep(2)
        self.dr.find_element_by_xpath('//*[@id="stat-overview"]/div[1]/button[2]').click()
        self.dr.find_element_by_class_name('layui-layer-btn0').click()
        sleep(4)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div[2]/div').click()
        sleep(3)
        self.dr.find_element_by_id('begin2').click()
        self.dr.find_element_by_id('begin2').send_keys('2020-06-10 00:00:00')
        self.dr.find_element_by_xpath('//*[@id="stat-detectorview"]/div[1]/button[1]').click()
        self.dr.find_element_by_id('begin2').click()
        self.dr.find_element_by_xpath('//*[@id="layui-laydate3"]/div[2]/div/span[3]').click()
        self.dr.find_element_by_xpath('//*[@id="stat-detectorview"]/div[1]/input[3]').send_keys('MP02MN6191231000032')
        self.dr.find_element_by_xpath('//*[@id="stat-detectorview"]/div[1]/button[2]').click()
        self.dr.find_element_by_class_name('layui-layer-btn0').click()
    def tearDown(self):
        self.dr.close()
if __name__ == '__main__':
        unittest.main()