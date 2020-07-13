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
    def test_xxgl(self):
        deng_lu = Deng_lu(self.dr)
        deng_lu.denglu()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[3]/span').click()#点击电力设备
        self.dr.find_element_by_xpath('//*[@id="admin-menus-box"]/div/div[3]/div/div[2]').click()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[1]/div[2]/button').click()
        self.dr.switch_to.frame('layui-layer-iframe100001')
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div[1]/div[2]/input').send_keys('自动测试')
        self.dr.find_element_by_id('hm').click()
        js = "$('input[id=hm').removeAttr('readonly')"  # 2.jQuery，移除属性
        #js = "$('input[id=history_record_time').attr('readonly',false)"  # 3.jQuery，设置为false
        self.dr.execute_script(js)
        sleep(3)
        target = self.dr.find_element_by_xpath('//*[@id="layui-laydate1"]/div[1]/div[2]/ul/li[1]/ol/li[22]')
        # 滚动到目标位置
        self.dr.execute_script("arguments[0].scrollIntoView();", target)
        sleep(1)
        self.dr.find_element_by_xpath('//*[@id="layui-laydate1"]/div[1]/div[2]/ul/li[1]/ol/li[22]').click()
        self.dr.find_element_by_xpath('//*[@id="layui-laydate1"]/div[1]/div[2]/ul/li[2]/ol/li[1]').click()
        self.dr.find_element_by_xpath('//*[@id="layui-laydate1"]/div[1]/div[2]/ul/li[3]/ol/li[1]').click()
        sleep(4)
        #self.dr.find_element_by_id('hm').send_keys('21:00')
        self.dr.find_element_by_class_name('laydate-btns-confirm').click()
        sleep(2)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div[5]/div[2]/div[52]/img').click()
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/div[6]/button').click()
        sleep(3)
        self.dr.find_element_by_xpath('//*[@id="pageShow"]/div[2]/table/tbody/tr[1]/td[5]/button[3]').click()
        sleep(3)
        self.dr.find_element_by_class_name('tabs-right').click()
    def tearDown(self):
        pass
if __name__ == "__main__":
        unittest.main()