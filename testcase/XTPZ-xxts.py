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
    def test_xxts(self):
        deng_lu = Deng_lu(self.dr)
        deng_lu.denglu()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[7]/span').click()
        self.dr.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[7]/div/div[2]').click()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/table/tbody/tr[1]/td/span[2]/input').send_keys('smtp.mxhichina.com')
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/table/tbody/tr[2]/td/span[2]/input').send_keys('tudou@mnaie.com')
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/table/tbody/tr[3]/td/span[2]/input').send_keys('迈内能源')
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/table/tbody/tr[4]/td/span[2]/input').send_keys('tudou@mnaie.com')
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/table/tbody/tr[5]/td/span[2]/input').send_keys('tudou@mnaie.com')
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/table/tbody/tr[6]/td/span[2]/input').send_keys('465')
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/table/tbody/tr[7]/td/span[2]/input').send_keys('tls')
        a = Select(self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/table/tbody/tr[8]/td/span[2]/select'))  # 定位下拉框
        a.select_by_visible_text("发送")  # 文本定位
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/table/tbody/tr[9]/td/button').click()


    def tearDown(self):
        pass


if __name__ == '__main__':
        unittest.main()