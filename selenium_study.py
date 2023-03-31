# 
# -*- coding: utf-8 -*-
# ---
# @Project: selenium_learning
# @Software: PyCharm
# @File: selenium_study.py
# @Author: lxs
# @Time: 2022/10/26 20:32
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建浏览器对象
driver = webdriver.Chrome()
# 浏览器窗口最大化
driver.maximize_window()
# 访问页面 输入url地址
url = 'http://www.mtxshop.com:3000/'
# 打开url对应的页面
driver.get(url)
# time.sleep(5)
# # 关闭浏览器
# # driver.quit()
# # # 刷新浏览器页面
# # driver.refresh()
# # # 页面回退
# driver.back()
# # # 页面下向前
# driver.forward()
# # 获取页面源码：可用来做断言，判断一个文本内容是否存在于页面源码中
# page_source = driver.page_source
# print(page_source)

el = driver.find_element(By.LINK_TEXT, '登录')
el.click()
time.sleep(3)
driver.find_element(By.LINK_TEXT,'账号登录').click()
# 输入用户名 send_keys()
driver.find_element(By.ID, "username").send_keys('yaoyao')
# 输入密码
driver.find_element(By.ID, 'password').send_keys('yaoyao123456')
# 验证码输入
driver.find_element(By.ID, 'validcode').send_keys('1512')
# 登录按钮
driver.find_elements(By.CLASS_NAME, 'form-sub')[1].click()
