# 
# -*- coding: utf-8 -*-
# ---
# @Project: selenium_learning
# @Software: PyCharm
# @File: test_modify_birth.py
# @Author: chenhuaishu
# @Time: 2023/3/3 15:33
from selenium import webdriver

from selenium_el import login, modify_birth


class TestModifyBirth:
    driver = None
    def setup_class(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        TestModifyBirth.driver = webdriver.Chrome(options=options)
        TestModifyBirth.driver.maximize_window()
        TestModifyBirth.driver.get('http://www.mtxshop.com:3000/')
        login(TestModifyBirth.driver)
    def test_modify_birth(self):
        modify_birth(TestModifyBirth.driver)
