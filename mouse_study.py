# 
# -*- coding: utf-8 -*-
# ---
# @Project: selenium_learning
# @Software: PyCharm
# @File: mouse_study.py
# @Author: chenhuaishu
# @Time: 2023/3/4 17:01
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# 创建driver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(r'E:\learning\python\pycharm\project\selenium_learning\拖拽.html')
# 创建鼠标对象
action = ActionChains(driver)
small_box = driver.find_element(By.CLASS_NAME, 'drag')
big_box = driver.find_element(By.CLASS_NAME, 'drag-box')
# 1.鼠标悬浮
action.move_to_element(small_box).perform()
# 2.双击
action.double_click(small_box).perform()
# 3.拖拽
action.drag_and_drop(small_box, big_box).perform()

