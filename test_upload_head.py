# 
# -*- coding: utf-8 -*-
# ---
# @Project: selenium_learning
# @Software: PyCharm
# @File: test_upload_head.py
# @Author: chenhuaishu
# @Time: 2023/3/3 19:57
from selenium import webdriver
from selenium_el import login, upload_head, upload_head1


class TestUploadHead:
    driver = None
    def setup_class(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        TestUploadHead.driver = webdriver.Chrome(options=options)
        TestUploadHead.driver.maximize_window()
        TestUploadHead.driver.get('http://www.mtxshop.com:3000/')
        login(TestUploadHead.driver)
    def test_upload_head(self):
        # upload_head(TestUploadHead.driver)
        upload_head1(TestUploadHead.driver)
