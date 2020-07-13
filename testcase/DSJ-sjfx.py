import unittest
from selenium import webdriver
from time import sleep
from public import Login
from  public.Login import Deng_lu
from selenium.webdriver.common.keys import Keys

class DSJ(unittest.TestCase):
    driver = webdriver.Chrome()
    def setUp(self):
        self.driver.get('http://47.103.3.209/admin/detector-list')
    def test_sjfx(self):
        deng_lu = Deng_lu(self.driver)
        deng_lu.denglu()
        sleep(5)
        # 点击大数据
        self.driver.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[2]').click()
        sleep(2)
        # 点击数据分析
        self.driver.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[2]/div/div[1]').click()
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div[3]/table/tbody/tr[3]/td[2]/button').click()
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div[2]/div[2]/div[4]/span').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div[2]/div[3]/div[1]/div[2]/span').click()
        sleep(3)
        self.driver.find_element_by_id('history_record_time').send_keys('2020-06-18 16:36:47 - 2020-06-23 16:36:47')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="layui-laydate1"]/div[3]/div/span').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div[2]/div[4]/div/select')#定位下拉框
        sleep(1)
        self.driver.find_elements_by_tag_name('option')[1].click()#获取下拉框第二个选项
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div[3]/div[1]/div[2]').click()
        sleep(4)
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
        unittest.main()