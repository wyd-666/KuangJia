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
    def test_xtcs(self):
        deng_lu = Deng_lu(self.dr)
        deng_lu.denglu()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[7]/span').click()
        self.dr.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[7]/div/div[1]').click()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/table/tbody/tr[1]/td[3]/button').click()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[4]/div[1]/div/div[2]/input').clear()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[4]/div[1]/div/div[2]/input').send_keys('FFA500')
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[4]/div[2]/span[2]').click()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/table/tbody/tr[1]/td[3]/button').click()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[4]/div[1]/div/div[2]/input').clear()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[4]/div[1]/div/div[2]/input').send_keys('ffffff')
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[4]/div[2]/span[2]').click()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/table/tbody/tr[2]/td[3]/button').click()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[3]/div[2]/span[2]').click()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/table/tbody/tr[3]/td[3]/button').click()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[4]/div[2]/span[2]').click()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/table/tbody/tr[4]/td[3]/button').click()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[4]/div[2]/span[1]').click()
        sleep(3)

    def tearDown(self):
        self.dr.close()


if __name__ == '__main__':
        unittest.main()