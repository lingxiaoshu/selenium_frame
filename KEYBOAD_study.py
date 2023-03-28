# 
# -*- coding: utf-8 -*-
# ---
# @Project: selenium_learning
# @Software: PyCharm
# @File: KEYBOAD_study.py
# @Author: chenhuaishu
# @Time: 2023/3/4 17:07
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# 创建driver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(r'E:\learning\python\pycharm\project\selenium_learning\注册A.html')
# 定位输入用户名
username = driver.find_element(By.ID, 'userA')
username.send_keys('ceshicourse')
# 删除最后一个字符
username.send_keys(Keys.BACKSPACE)
# 全选
username.send_keys(Keys.CONTROL, 'A')
# 复制
username.send_keys(Keys.CONTROL, 'C')
# 定位下一个输入框，粘贴
driver.find_element(By.ID, 'telA').send_keys(Keys.CONTROL, 'V')
