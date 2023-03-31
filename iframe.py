# 
# -*- coding: utf-8 -*-
# ---
# @Project: selenium_learning
# @Software: PyCharm
# @File: iframe.py
# @Author: lxs
# @Time: 2023/3/4 10:20
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_163login():
    # 创建driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get('https://mail.163.com/')
    # 隐式等待
    driver.implicitly_wait(10)
    # 1.切换iframe，页面第一个iframe，index=0
    # driver.switch_to.frame(0)
    # 2.定位iframe这个元素
    iframe_el = driver.find_element(By.XPATH, '(//iframe)[1]')
    # driver.switch_to.frame(iframe_el)
    # 显示等待的引入
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.frame_to_be_available_and_switch_to_it(iframe_el))
    # 用户输入
    driver.find_element(By.CSS_SELECTOR, 'input[name="email"]').send_keys("huaishuchen@163.com")
    # 密码输入
    driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys("160818wasj")
    # 点击登录
    driver.find_element(By.ID, "dologin").click()
    # 回到最初的iframe
    driver.switch_to.default_content()
    # 回到上一级的frame
    driver.switch_to.parent_frame()
