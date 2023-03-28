# 
# -*- coding: utf-8 -*-
# ---
# @Project: selenium_learning
# @Software: PyCharm
# @File: test_add_address.py
# @Author: chenhuaishu
# @Time: 2022/10/30 15:34
from selenium import webdriver

from selenium_el import login, add_address


class TestAddAddress:
    driver = None
    def setup_class(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        TestAddAddress.driver = webdriver.Chrome(options=options)
        TestAddAddress.driver.maximize_window()
        TestAddAddress.driver.get('http://www.mtxshop.com:3000/')
        login(TestAddAddress.driver)
    def test_add_address(self):
        add_address(TestAddAddress.driver)

