# 
# -*- coding: utf-8 -*-
# ---
# @Project: selenium_learning
# @Software: PyCharm
# @File: test_create_order.py
# @Author: chenhuaishu
# @Time: 2022/10/30 16:33
from selenium import webdriver

from selenium_el import login, create_order


class TestCreateOrder:
    driver = None
    def setup_class(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        TestCreateOrder.driver = webdriver.Chrome(options=options)
        TestCreateOrder.driver.maximize_window()
        TestCreateOrder.driver.get('http://www.mtxshop.com:3000/')
        login(TestCreateOrder.driver)
    def test_create_order(self):
        create_order(TestCreateOrder.driver)
