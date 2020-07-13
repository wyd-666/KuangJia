import unittest
from selenium import webdriver
from time import sleep
from public import Login
from  public.Login import Deng_lu
from selenium.webdriver.common.keys import Keys

class Bj(unittest.TestCase):
    driver = webdriver.Chrome()
    def setUp(self):
        self.driver.get('http://47.103.3.209/admin/detector-list')
    def test_bj(self):
        deng_lu = Deng_lu(self.driver)
        deng_lu.denglu()
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[1]/span').click()
        sleep(4)
        # 点击第二条的复选框
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div[2]/table/tbody/tr[1]/td[1]').click()
        # 标记处理第二条报警
        #self.driver.find_element_by_xpath('//*[@id="pageShow"]/div[2]/table/tbody/tr[1]/td[9]/button[1]').click()
        sleep(5)
        # 点击是
        #self.driver.find_element_by_class_name('layui-layer-btn0').click()
        # 删除第一条报警
        #self.driver.find_element_by_xpath('//*[@id="pageShow"]/div[2]/table/tbody/tr[1]/td[9]/button[2]').click()
        # 点击是
        #self.driver.find_element_by_class_name('layui-layer-btn0').click()
        '''
        # 点击第三条的详情
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div[2]/table/tbody/tr[3]/td[9]/button[3]').click()
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="layui-layer100001"]/span[1]/a').click()
        sleep(3)
        # 点击第三条的管理
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div[2]/table/tbody/tr[3]/td[9]/button[4]').click()
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="layui-layer100002"]/span[1]/a').click()
        sleep(3)
        # 设置目标为某个元素，我使用xpath的定位方法
        target = self.driver.find_element_by_xpath('//*[@id="layui-laypage-1"]/span[3]/button')
        # 滚动到目标位置
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        self.driver.find_element_by_xpath('//*[@id="layui-laypage-1"]/a[7]').click()
        sleep(3)
        target = self.driver.find_element_by_xpath('//*[@id="layui-laypage-1"]/span[3]/button')
        # 滚动到目标位置
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="layui-laypage-1"]/a[1]').click()
        sleep(3)
        target = self.driver.find_element_by_xpath('//*[@id="layui-laypage-1"]/span[3]/button')
        # 滚动到目标位置
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="layui-laypage-1"]/span[3]/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="layui-laypage-1"]/span[3]/input').send_keys('3')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="layui-laypage-1"]/span[3]/button').click()
        '''
        sleep(4)
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()