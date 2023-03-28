# 
# -*- coding: utf-8 -*-
# ---
# @Project: selenium_learning
# @Software: PyCharm
# @File: screenshot.py
# @Author: chenhuaishu
# @Time: 2023/3/4 16:34
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建driver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(r'E:\learning\python\pycharm\project\selenium_learning\alert.html')
# # 定位元素
# driver.find_element(By.XPATH, '//input[1]').click()
# time.sleep(2)
## 两种截图的方法
# 1.截图返回的是二进制对象，贴到allure报告中
img = driver.get_screenshot_as_png()
print(img, type(img))
# 截图成一张图片保存到固定位置
img1 = driver.get_screenshot_as_file('1.png')