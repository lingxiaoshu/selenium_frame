# 
# -*- coding: utf-8 -*-
# ---
# @Project: selenium_learning
# @Software: PyCharm
# @File: select_study.py
# @Author: chenhuaishu
# @Time: 2023/3/4 17:24
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# 创建driver
# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(r'E:\learning\python\pycharm\project\selenium_learning\注册A.html')
selecta = driver.find_element(By.ID, 'selectA')
el = Select(selecta)
el.select_by_value("gz")
time.sleep(3)

el.select_by_index(1)
time.sleep(3)
el.select_by_visible_text('A重庆')