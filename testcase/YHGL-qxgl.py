import unittest
from selenium import webdriver
from time import sleep
from time import sleep
from public.Login import Deng_lu
from selenium.webdriver.support.select import Select

class YHGL(unittest.TestCase):
    dr = webdriver.Chrome()
    def setUp(self):
        self.dr.get('http://47.103.3.209/admin/detector-list')
    def test_qxgl(self):
        deng_lu = Deng_lu(self.dr)
        deng_lu.denglu()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[4]/span').click()
        self.dr.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[4]/div/div[2]').click()
        sleep(3)
        self.dr.find_element_by_class_name('tabs-right').click()
        sleep(2)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div[1]/div[2]/input').send_keys('自动测试员')
        self.dr.find_element_by_xpath('//*[@id="admin.terminal.read"]').click()
        self.dr.find_element_by_xpath('//*[@id="admin.user.read"]').click()
        # 设置目标为某个元素，我使用xpath的定位方法
        target = self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div[3]/button')
        # 滚动到目标位置
        self.dr.execute_script("arguments[0].scrollIntoView();", target)
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div[3]/button').click()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/table/tbody/tr[7]/td[2]/button[2]').click()
        self.dr.find_element_by_class_name('layui-layer-btn0').click()
    def tearDown(self):
        self.dr.close()

if __name__ == '__main__':
        unittest.main()