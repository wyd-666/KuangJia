from selenium import webdriver
import unittest
from time import sleep
from time import sleep
from public.Login import Deng_lu
from selenium.webdriver.support.select import Select

class ZDGL(unittest.TestCase):
    dr = webdriver.Chrome()
    def setUp(self):
        self.dr.get('http://47.103.3.209/admin/')
    def test_sjdc(self):
        deng_lu = Deng_lu(self.dr)
        deng_lu.denglu()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[6]/span').click()
        self.dr.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[6]/div/div[4]').click()
        sleep(3)
        a = Select(self.dr.find_element_by_xpath('//*[@id="equipment"]/div[2]/select[1]'))  # 定位下拉框
        a.select_by_visible_text("A测试")  # 文本定位
        b = Select(self.dr.find_element_by_xpath('//*[@id="equipment"]/div[2]/select[2]'))  # 定位下拉框
        b.select_by_visible_text("自动测试")  # 文本定位
        c = Select(self.dr.find_element_by_xpath('//*[@id="equipment"]/div[2]/select[3]'))  # 定位下拉框
        c.select_by_visible_text("自动测试")  # 文本定位
        c = Select(self.dr.find_element_by_xpath('//*[@id="equipment"]/div[2]/select[4]'))  # 定位下拉框
        c.select_by_visible_text("请选择设备状态")  # 文本定位
        self.dr.find_element_by_xpath('//*[@id="stTime"]').click()
        self.dr.find_element_by_xpath('//*[@id="layui-laydate1"]/div[1]/div[2]/table/tbody/tr[1]/td[4]').click()
        self.dr.find_element_by_class_name('laydate-btns-confirm').click()
        sleep(2)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div[2]/table/tbody/tr[2]/td[2]/span[1]/img').click()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div[2]/table/tbody/tr[2]/td[2]/span[1]/img').click()
        # 设置目标为某个元素，我使用xpath的定位方法
        target = self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div[4]/table/tbody/tr[4]/td[2]/span/img')
        # 滚动到目标位置
        self.dr.execute_script("arguments[0].scrollIntoView();", target)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div[4]/table/tbody/tr[4]/td[2]/span/img').click()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div[4]/table/tbody/tr[4]/td[2]/span/img').click()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/input').click()
        self.dr.find_element_by_class_name('layui-layer-btn0').click()
        # 设置目标为某个元素，我使用xpath的定位方法
        target = self.dr.find_element_by_xpath('//*[@id="equipment"]/div[1]/div[1]/div[2]')
        # 滚动到目标位置
        self.dr.execute_script("arguments[0].scrollIntoView();", target)
        sleep(5)
        self.dr.find_element_by_xpath('//*[@id="equipment"]/div[1]/div[1]/div[2]').click()
    def tearDown(self):
        pass
if __name__ == '__main__':
        unittest.main()