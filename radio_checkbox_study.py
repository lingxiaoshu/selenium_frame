# 
# -*- coding: utf-8 -*-
# ---
# @Project: selenium_learning
# @Software: PyCharm
# @File: radio_checkbox_study.py
# @Author: chenhuaishu
# @Time: 2023/3/4 16:44
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建driver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(r'E:\learning\python\pycharm\project\selenium_learning\注册A.html')
# 定位单选框-橘子
el = driver.find_element(By.ID, 'jza')
# if not el.is_selected():
#     # 单选框未被选择，点击
#     el.click()
print("元素是否被选择{}".format(el.is_selected()))
print("元素是否被使用{}".format(el.is_enabled()))
print("元素是否被展示{}".format(el.is_displayed()))
driver.find_element(By.ID, 'qcA').click()
driver.find_element(By.ID, 'gwA').click()
driver.find_element(By.ID, 'lyA').click()
