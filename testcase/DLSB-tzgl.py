import unittest
from selenium import webdriver
from time import sleep
from time import sleep
from public.Login import Deng_lu
from selenium.webdriver.support.select import Select

class DLSB(unittest.TestCase):
    dr = webdriver.Chrome()
    def setUp(self):
        self.dr.get('http://47.103.3.209/admin/detector-list')
    def test_tzgl(self):
        deng_lu = Deng_lu(self.dr)
        deng_lu.denglu()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[3]/span').click()
        self.dr.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[3]/div/div[1]').click()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[1]/div[2]/button').click()
        sleep(3)
        self.dr.switch_to.frame('layui-layer-iframe100001')
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div/div[2]/div[2]/input').click()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div/div[2]/div[2]/input').send_keys('A测试')
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div/div[3]/button').click()
        sleep(3)
        #self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[1]/div[2]/button').click()
        #self.dr.switch_to.default_content()
        #self.dr.find_element_by_xpath('//*[@id="layui-layer100002"]/span[1]/a').click()
        sleep(3)
        # 设置目标为某个元素，我使用xpath的定位方法
        target = self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/table/tbody/tr[357]/td[1]/span')
        # 滚动到目标位置
        self.dr.execute_script("arguments[0].scrollIntoView();", target)
        sleep(2)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/table/tbody/tr[357]/td[2]/button[5]').click()
        self.dr.switch_to.frame('layui-layer-iframe100002')
        sleep(2)
        #a=Select(self.dr.find_element_by_xpath('//*[@id="pageShow"]/div/div[2]/div[2]/select'))#定位下拉框
        #a.select_by_visible_text('GIS设备')#文本定位
        #sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div/div[3]/div[2]/input').click()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div/div[3]/div[2]/input').send_keys('自动测试')
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div/div[5]/button').click()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/table/tbody/tr[357]/td[1]').click()
        sleep(2)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/table/tbody/tr[358]/td[2]/button[3]').click()
        self.dr.switch_to.frame('layui-layer-iframe100003')
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div/div[2]/div[2]/input').send_keys('自动测试')
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div/div[3]/div[2]/input').send_keys('123456789')
        #self.dr.find_element_by_xpath('//*[@id="pageShow"]/div/div[4]/div[2]/input').send_keys('01')
        #self.dr.find_element_by_xpath('//*[@id="pageShow"]/div/div[5]/div[2]/input').send_keys('00000')
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div/div[11]/button').click()

    def tearDown(self):
        pass

if __name__ == '__main__':
        unittest.main()

