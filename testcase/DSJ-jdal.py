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
    def test_jdal(self):
        deng_lu = Deng_lu(self.driver)
        deng_lu.denglu()
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[2]/span').click()
        self.driver.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[2]/div/div[2]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div[2]/table/tbody/tr[1]/td[2]/button').click()
        sleep(3)
        self.driver.back()
        sleep(3)
    def tearDown(self):
        self.driver.close()
if __name__ == '__main__':
        unittest.main()
