import unittest
from selenium import webdriver
from public import Login
from time import sleep
from public.Login import Deng_lu
from selenium.webdriver.support.select import Select


class DSJ(unittest.TestCase):
    driver = webdriver.Chrome()
    def setUp(self):
        self.driver.get('http://47.103.3.209/admin/detector-list')
    def test_yjbg(self):
        deng_lu = Deng_lu(self.driver)
        deng_lu.denglu()
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[2]/span').click()
        self.driver.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[2]/div/div[4]').click()
        sleep(3)
        #self.driver.find_element_by_xpath('//*[@id="history_record_time"]').click()
        sleep(6)
        js = "$('input[id=history_record_time').removeAttr('readonly')"  # 2.jQuery，移除属性
        #js = "$('input[id=history_record_time').attr('readonly',false)"  # 3.jQuery，设置为false
        self.driver.execute_script(js)
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="history_record_time"]').clear()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="history_record_time"]').send_keys('2020-06-29 00:00:00 - 2020-06-30 00:00:00')
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div[3]/div/div[5]/div[2]/div/textarea').click()
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="history_record_time"]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="layui-laydate1"]/div[3]/div/span').click()
        a=Select(self.driver.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div/select'))#定位下拉框
        a.select_by_visible_text('T2000跑测')#文本定位
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div[3]/div/div[2]/table/tbody/tr[2]/td[2]/input').send_keys('帝')
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div[3]/div/div[5]/div[2]/div/textarea').send_keys('无')
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div/button').click()
    def tearDown(self):
        pass
if __name__ == '__main__':
        unittest.main()