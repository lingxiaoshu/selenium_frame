# 
# -*- coding: utf-8 -*-
# ---
# @Project: selenium_learning
# @Software: PyCharm
# @File: alert_study.py
# @Author: lxs
# @Time: 2023/3/4 16:21
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建driver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(r'E:\learning\python\pycharm\project\selenium_learning\alert.html')
# 1.定位确认框
# driver.find_element(By.XPATH, '//input[1]').click()
# # 2.切换alert弹窗上
# alert_obj = driver.switch_to.alert
# time.sleep(2)
# # 确定
# alert_obj.accept()
# # 取消
# alert_obj.dismiss()
# # 输入信息
# alert_obj.send_keys('这是一个测试项目')
# 1.定位输入内容
driver.find_element(By.XPATH, '//input[3]').click()
# 2.切换alert弹窗上
alert_obj = driver.switch_to.alert
time.sleep(2)
# 输入信息
alert_obj.send_keys('这是一个测试项目')
# 确定
alert_obj.accept()
tl = driver.find_element(By.ID, 'demo')
print("最终页面展示的信息是".format(tl.text))