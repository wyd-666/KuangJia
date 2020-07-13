import unittest
from selenium import webdriver
from time import sleep

from time import sleep
class login(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://47.103.3.209/admin/detector-list")
        self.driver.maximize_window()
    def tearDown(self):
        sleep(5)
    def test_1(self):
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div/div[2]/input').click()
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div/div[2]/input').send_keys('admin')
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div/div[3]/input').click()
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div/div[3]/input').send_keys('123456')
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div/div[5]').click()


if __name__ == "__main__":
    unittest.main()