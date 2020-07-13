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
    def test_yhgl(self):
        deng_lu = Deng_lu(self.dr)
        deng_lu.denglu()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[4]/span').click()
        self.dr.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[4]/div/div[1]').click()
        sleep(3)
        self.dr.find_element_by_class_name('tabs-right').click()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div[1]/div[2]/input').send_keys('6666666')
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div[2]/div[2]/input').send_keys('123456')
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div[3]/div[2]/input').send_keys('测试')
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div[4]/div[2]/input').send_keys('16666666666')
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div[5]/div[2]/input').send_keys('666@qq.com')
        a=Select(self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div[6]/div[2]/select'))#定位下拉框
        a.select_by_visible_text('专工')#文本定位
        b=Select(self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div[7]/div[2]/select'))#定位下拉框
        b.select_by_visible_text('测试')#文本定位
        sleep(2)
        self.dr.find_element_by_xpath('//*[@id="52"]').click()
        sleep(2)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div[10]/button').click()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/table/tbody/tr[14]/td[6]/button[2]').click()
        self.dr.find_element_by_class_name('layui-layer-btn0').click()
    def tearDown(self):
        self.dr.close()
if __name__ == '__main__':
        unittest.main()