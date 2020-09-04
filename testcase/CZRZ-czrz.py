from selenium import webdriver
import unittest
from time import sleep
from time import sleep
from public.Login import Deng_lu
from selenium.webdriver.support.select import Select

class CZRZ(unittest.TestCase):
    dr = webdriver.Chrome()
    def setUp(self):
        self.dr.get('http://192.168.0.205/admin')
    def test_czrz(self):
        deng_lu = Deng_lu(self.dr)
        deng_lu.denglu()
        sleep(3)
        # 点击操作日志
        self.dr.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[8]/span').click()
        sleep(3)
        a = Select(self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/select'))  # 定位下拉框
        a.select_by_visible_text("admin【】")  # 文本定位
        self.dr.find_element_by_xpath('//*[@id="startTime"]').send_keys('2020-08-05')
        self.dr.find_element_by_xpath('//*[@id="endTime"]').send_keys('2020-08-07')
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/button').click()
        sleep(4)
        # 设置目标为某个元素，我使用xpath的定位方法
        target = self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[3]/table/tbody/tr[16]/td[2]/button')
        # 滚动到目标位置
        self.dr.execute_script("arguments[0].scrollIntoView();", target)

        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[3]/table/tbody/tr[15]/td[1]/img[2]').click()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[3]/table/tbody/tr[16]/td[2]/button').click()
        self.dr.find_element_by_class_name('layui-layer-btn1').click()
        sleep(4)
        self.dr.find_element_by_class_name('layui-laypage-next').click()

    def tearDown(self):
        pass

if __name__ == '__main__':
        unittest.main()