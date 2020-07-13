from selenium import webdriver
import unittest,time
from time import sleep

class Deng_lu():
    u"""登录"""
    def __init__(self,driver):
        self.driver = driver
    def denglu(self):
        self.driver.maximize_window()
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div/div[2]/input').click()
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div/div[2]/input').send_keys('admin')
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div/div[3]/input').click()
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div/div[3]/input').send_keys('123456')
        self.driver.find_element_by_xpath('//*[@id="pageShow"]/div/div[5]').click()
        sleep(5)
