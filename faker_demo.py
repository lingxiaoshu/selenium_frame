# 
# -*- coding: utf-8 -*-
# ---
# @Project: selenium_learning
# @Software: PyCharm
# @File: faker_demo.py
# @Author: chenhuaishu
# @Time: 2022/10/30 14:29
from faker import Faker

#创建Faker对象
faker = Faker('zh_CN')
print(faker.address())
print(faker.name())
print(faker.city())
print(faker.building_name())