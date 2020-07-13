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
    def test_fzgl(self):
        deng_lu = Deng_lu(self.driver)
        deng_lu.denglu()
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[2]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[2]/div/div[3]').click()
        sleep(2)
        #添加分组-
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div[1]/div[2]/button').click()
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div/div[1]/div[2]/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div/div[1]/div[2]/input').send_keys('测试分组1')
        a=Select(self.driver.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div/div[2]/div[2]/select'))#定位下拉框
        a.select_by_visible_text('T2000跑测')#文本定位
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div/div[3]/div[1]/label').click()
        self.driver.find_element_by_xpath('//*[@id="29"]').click()
        # 使用保存的元素
        target = self.driver.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div/div[5]/button')
        # 滚动到保存位置
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div/div[5]/button').click()
        #添加分组---
        sleep(4)
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div[3]/table/tbody/tr[1]/td[3]/button[1]').click()
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div/div[1]/div[2]/input').click()
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div/div[1]/div[2]/input').clear()#  清空文本框内容
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div/div[1]/div[2]/input').send_keys('自动测试')
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div/div[4]/div[2]/div[1]/span[2]').click()
        sleep(1)
        self.driver.find_element_by_class_name('layui-btn').click()
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div[3]/table/tbody/tr[1]/td[3]/button[3]').click()
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div[3]/table/tbody/tr[1]/td[3]/button[2]').click()
        sleep(2)
        self.driver.find_element_by_class_name('layui-layer-btn0').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div[2]/input').click()
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div[2]/input').send_keys('gis1')
        sleep(4)







    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
        unittest.main()