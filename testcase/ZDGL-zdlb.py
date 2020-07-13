from selenium import webdriver
import unittest
from time import sleep
from time import sleep
from public.Login import Deng_lu
from selenium.webdriver.support.select import Select

class ZDGL(unittest.TestCase):
    dr = webdriver.Chrome()
    def setUp(self):
        self.dr.get('http://192.168.0.205/admin/detector-list')
    def test_zdlb(self):
        deng_lu = Deng_lu(self.dr)
        deng_lu.denglu()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[6]/span').click()
        self.dr.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[6]/div/div[3]').click()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/select[1]').click()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/select[2]').click()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/select[3]').click()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/select[4]').click()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/select[5]').click()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/select[6]').click()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/select[7]').click()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/button[1]').click()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/button[2]').click()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/button[3]').click()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/input[1]').send_keys('000032')
        sleep(2)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[3]/table/tbody/tr[1]/td/div/div[1]').click()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[3]/table/tbody/tr[2]/td[8]/table/tbody/tr[1]/td[1]/span/span').click()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div[1]/div[2]/div[2]/span').click()
        sleep(1)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div[1]/div[2]/div[3]/span').click()
        self.dr.find_element_by_id('history_record_time').click()
        sleep(2)
        self.dr.find_element_by_xpath('//*[@id="layui-laydate1"]/div[1]/div[2]/table/tbody/tr[1]/td[4]').click()
        self.dr.find_element_by_class_name('laydate-btns-confirm').click()
        sleep(3)
        # 设置目标为某个元素，我使用xpath的定位方法
        target = self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[7]/div/button')
        # 滚动到目标位置
        self.dr.execute_script("arguments[0].scrollIntoView();", target)
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[7]/div/button').click()
        sleep(2)
        self.dr.find_element_by_xpath('//*[@id="layui-layer100001"]/span[1]/a').click()
        sleep(3)
        self.dr.back()
        sleep(4)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/input[1]').clear()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/input[1]').send_keys('000032')
        sleep(2)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[3]/table/tbody/tr[1]/td/div/div[1]').click()
        sleep(2)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[3]/table/tbody/tr[2]/td[8]/table/tbody/tr[1]/td[2]/span').click()
        self.dr.find_element_by_class_name('layui-layer-btn1').click()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[3]/table/tbody/tr[2]/td[8]/table/tbody/tr[1]/td[3]/span/span').click()
        sleep(1)
        self.dr.find_element_by_xpath('//*[@id="layui-layer100002"]/span[1]/a').click()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[3]/table/tbody/tr[2]/td[8]/table/tbody/tr[1]/td[4]/span/span').click()
        self.dr.find_element_by_class_name('layui-layer-btn1').click()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[3]/table/tbody/tr[2]/td[8]/table/tbody/tr[1]/td[4]/span/span').click()
        sleep(2)
        self.dr.find_element_by_class_name('layui-layer-btn1').click()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[3]/table/tbody/tr[2]/td[8]/table/tbody/tr[2]/td[1]/span/span').click()
        sleep(2)
        self.dr.find_element_by_class_name('layui-layer-btn1').click()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[3]/table/tbody/tr[2]/td[8]/table/tbody/tr[2]/td[2]/span/span').click()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[3]/table/tbody/tr[1]/td[1]/div/span').click()
        self.dr.back()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[3]/table/tbody/tr[1]/td/div/div[1]').click()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[3]/table/tbody/tr[2]/td[8]/table/tbody/tr[2]/td[3]/span/span').click()
        sleep(2)
        self.dr.find_element_by_xpath('//*[@id="layui-layer100001"]/span[1]/a').click()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[3]/table/tbody/tr[2]/td[8]/table/tbody/tr[2]/td[4]/span/span').click()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[3]/table/tbody/tr[1]/td[1]/div/span').click()
        self.dr.back()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[3]/table/tbody/tr[1]/td/div/div[1]').click()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[3]/table/tbody/tr[2]/td[8]/table/tbody/tr[3]/td[1]/span/span').click()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="layui-layer100001"]/span[1]/a').click()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[3]/table/tbody/tr[2]/td[8]/table/tbody/tr[3]/td[2]/span/span').click()
        self.dr.find_element_by_class_name('layui-layer-btn1').click()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[3]/table/tbody/tr[2]/td[8]/table/tbody/tr[3]/td[3]/span/span').click()
        sleep(2)
        self.dr.find_element_by_class_name('layui-layer-btn1').click()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[3]/table/tbody/tr[2]/td[8]/table/tbody/tr[4]/td/span/span').click()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[3]/table/tbody/tr[1]/td[1]/div[1]/span').click()
        sleep(5)
        self.dr.back()
        sleep(5)








    def tearDown(self):
        self.dr.close()
if __name__ == '__main__':
        unittest.main()