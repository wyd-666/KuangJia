from selenium import webdriver
import unittest
from time import sleep
from time import sleep
from public.Login import Deng_lu
from selenium.webdriver.support.select import Select

class ZDGL(unittest.TestCase):
    dr = webdriver.Chrome()
    def setUp(self):
        self.dr.get('http://47.103.3.209/admin/')
    def test_cspz(self):
        deng_lu = Deng_lu(self.dr)
        deng_lu.denglu()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[6]/span').click()
        self.dr.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[6]/div/div[5]').click()
        sleep(3)
        a = Select(self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div/select[1]'))  # 定位下拉框
        a.select_by_visible_text("A测试")  # 文本定位
        b = Select(self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div/select[2]'))  # 定位下拉框
        b.select_by_visible_text("自动测试")  # 文本定位
        c = Select(self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div/select[3]'))  # 定位下拉框
        c.select_by_visible_text("自动测试")  # 文本定位
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div/input').send_keys('522130')
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[3]/div[2]/div[1]/div/div[2]/input').send_keys('300')
        d = Select(self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[3]/div[2]/div[2]/div/div[2]/select'))  # 定位下拉框
        d.select_by_visible_text("60分钟")  # 文本定位
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[3]/div[2]/div[3]/div/button').click()
    def tearDown(self):
        pass
if __name__ == '__main__':
        unittest.main()