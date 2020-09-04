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
    def test_algl(self):
        deng_lu = Deng_lu(self.dr)
        deng_lu.denglu()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[7]/span').click()
        self.dr.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[7]/div/div[4]').click()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[1]/div[2]/button').click()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div/div/div[2]/input').send_keys('自动测试')
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div/div/button[1]').click()
        sleep(5)
        self.dr.back()
        sleep(3)
        try:
            self.dr.refresh()  # 刷新方法 refresh
            print('test pass: refresh successful')
        except Exception as e:
            print("Exception found", format(e))
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/table/tbody/tr[1]/td[2]/button[2]').click()
        self.dr.find_element_by_class_name('layui-layer-btn0').click()
        sleep(3)


    def tearDown(self):
        self.dr.close()


if __name__ == '__main__':
        unittest.main()