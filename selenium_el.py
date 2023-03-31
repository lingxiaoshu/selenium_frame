# 
# -*- coding: utf-8 -*-
# ---
# @Project: selenium_learning
# @Software: PyCharm
# @File: selenium_el.py
# @Author: lxs
# @Time: 2022/10/26 21:04
import time

import pyperclip
import pytest
import pytest_assume.plugin
from faker import Faker
from pynput.keyboard import Controller, Key

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# 显示等待封装，无法点击not clickable
# 判断元素点击是否成功
# def click_is_scuccess(driver):
#     try:
#         # new一个参数locator，存储定位元素的变量
#         locator = By.CSS_SELECTOR, '#address_list>li:first-child'
#         # 不定长参数，可以使用 args元组，
#         driver.find_element(*locator).click()
#         return True
#     except Exception as e:
#         return False
class element_click_is_success:
    '''
    locator：定位策略
    '''
    def __init__(self, locator):
        self.locator = locator
        # 定义函数的过程：定义参数、返回值、运行代码
    def __call__(self, driver):
        # 函数就是对象=类名() 等价于函数的名字
        try:
            # new一个参数locator，存储定位元素的变量
            # locator = By.CSS_SELECTOR, '#address_list>li:first-child'
            # 不定长参数，可以使用 args元组，
            driver.find_element(*self.locator).click()
            return True
        except Exception as e:
            return False

# 判断文本内容是否在页面源码中
class pagesource_contains_text:
    '''
    text：文本内容
    '''
    def __init__(self, text):
        self.locator = text
        # 定义函数的过程：定义参数、返回值、运行代码
    def __call__(self, driver):
        # 函数就是对象=类名() 等价于函数的名字
        try:
            return self.text in driver.page_source
        except Exception as e:
            return False

def login(driver):
    '''
    谁调用登录方法，谁就传登录的对象
    :param driver:
    :return:
    '''
    el = driver.find_element(By.LINK_TEXT, '登录')
    el.click()
    time.sleep(4)
    driver.find_element(By.LINK_TEXT, '账号登录').click()
    # 输入用户名 send_keys()
    driver.find_element(By.ID, "username").send_keys('yaoyao')
    # 输入密码
    driver.find_element(By.ID, 'password').send_keys('yaoyao123456')
    # 验证码输入
    driver.find_element(By.ID, 'validcode').send_keys('1512')
    # 登录按钮
    driver.find_elements(By.CLASS_NAME, 'form-sub')[1].click()

def add_address(driver:WebDriver):
    '''
    添加地址的业务
    :param driver:
    :return:
    '''
    time.sleep(3)
    # 进入个人中心
    driver.find_element(By.LINK_TEXT, "进入个人中心").click()
    time.sleep(3)
    # wait = WebDriver(driver = driver, timeout = 10, )
    # 点击收货地址
    driver.find_element(By.XPATH, '//*[text()="收货地址"]').click()
    time.sleep(3)
    # 点击添加地址
    driver.find_element(By.XPATH, '//*[text()="添加地址"]').click()
    faker = Faker('zh_CN')
    expect_name = faker.name()  # 预期名字
    time.sleep(3)
    # 点击收货人姓名
    # driver.find_element(By.XPATH,'(//input[@class="el-input__inner"])[1]').send_keys(faker.name)
    driver.find_element(By.XPATH, '//*[text()="收货人姓名"]/following-sibling::*//input').send_keys(expect_name)
    time.sleep(2)
    # 点击联系方式
    driver.find_element(By.XPATH,'(//input[@class="el-input__inner"])[2]').send_keys('18312341234')
    time.sleep(3)
    # driver.find_element(By.XPATH, '//*[text()="联系方式"]/following-sibling::*//input').send_keys(faker.name)
    # 收货区地区的选择
    # 创建鼠标对象
    # 模拟鼠标悬浮动作
    action = ActionChains(driver)
    # 将鼠标移动到元素上
    time.sleep(3)
    el = driver.find_element(By.CSS_SELECTOR, 'div.app-address-title-view')
    action.move_to_element(el).perform()  # perform() 使鼠标动作起作用
    # 省
    driver.find_element(By.LINK_TEXT, '北京').click()
    time.sleep(2)
    # 市
    driver.find_element(By.LINK_TEXT, '海淀区').click()
    time.sleep(2)
    # 区
    driver.find_element(By.LINK_TEXT, '三环以内').click()
    time.sleep(3)
    # 点击详细地址
    expect_address = faker.address()   # 预期地址
    driver.find_element(By.XPATH, '(//input[@class="el-input__inner"])[3]').send_keys(expect_address)
    # driver.find_element(By.XPATH, '//*[text()="详细地址"]/following-sibling::*//input').send_keys(faker.name)
    # 点击地址别名
    time.sleep(2)
    driver.find_element(By.XPATH,'(//input[@class="el-input__inner"])[4]').send_keys('这是一个地址别名11')
    # driver.find_element(By.XPATH, '//*[text()="地址别名"]/following-sibling::*//input').send_keys(faker.name)
    # 确认按钮
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[text()="确认"]').click()
    time.sleep(3)
    # 断言：判断预期结果与实际结果是否一致
    # 消息框 保存成功 in 页面源码中driver.page_sourse
    pytest.assume("保存成功" in driver.page_source)
    # 数据
    td_list = driver.find_elements(By.XPATH, '//tbody/tr[1]/td')
    name = td_list[0].text
    print(f'name的值是：{name}')
    address = td_list[1].text
    print(f'address的值是：{address}')
    detail_address = td_list[2].text
    print(f'detail_address的值是：{detail_address}')
    add_nickname = td_list[3].text
    print(f'add_nickname的值是：{add_nickname}')
    tel = td_list[4].text
    print(f'tel的值是：{tel}')
    pytest.assume(name == expect_name)
    pytest.assume(address == '北京海淀区三环以内')
    pytest.assume(detail_address == expect_address)
    pytest.assume(add_nickname == '这是一个地址别名11')
    pytest.assume(tel == '183****1234')

def create_order(driver:WebDriver):
    # 隐式等待--针对找元素
    driver.implicitly_wait(10)
    # 定位搜索框，输入
    driver.find_element(By.XPATH, '(//input[@class])[1]').send_keys('纯牛奶')
    time.sleep(2)  # 页面加载过慢导致的找不到元素，隐式等待可
    # 点击搜索商品
    driver.find_element(By.XPATH, '(//*[text()="搜商品"])[1]').click()
    time.sleep(2)  # 页面加载过慢导致的找不到元素，隐式等待可
    # 点击目标搜索页的商品
    driver.find_element(By.LINK_TEXT,'孟婆纯牛奶').click()
    time.sleep(2)   # 页面加载过慢导致的找不到元素，隐式等待可
    # # 页面新打开窗口，做窗口切换(多窗口情况，需要切换窗口 driver.window_handles)
    # all_handles = driver.window_handles
    # print(f'所有的窗口句柄是{all_handles}')
    # driver.switch_to(all_handles[-1])
    windows = driver.window_handles
    for handle in windows:
        driver.switch_to(handle)
        # # 1.通过页面title进行遍历切换
        # title = driver.title
        # if title == "孟婆纯牛奶-码同学实战项目":
        #     break
        # 2.通过页面url进行遍历切换
        url = driver.current_url
        if url == "http://www.mtxshop.com:3000/goods/2236":
            break
        # 3，可以通过页面上的特殊元素作为切换依据
        # try:
        #   goods_id = driver.find_element(xx,xxx).text
        #   if goods_id = xxx:
        #        break()
        # except:
        #   pass   # 切换不成功

    # time.sleep(5)   # 页面加载过慢导致的找不到元素，隐式等待可，只有NosuchElementException报错可以用隐式等待解决
    # 判断元素点击是否成功
    wait = WebDriverWait(driver, 10)
    # 点击立即购买
    wait.until(element_click_is_success((By.XPATH, '//*[text()="立即购买"]')))
    # driver.find_element(By.XPATH, '//*[text()="立即购买"]').click()
    # time.sleep(4)   # 页面加载过慢导致的找不到元素，隐式等待可
    wait.until(element_click_is_success((By.CSS_SELECTOR, '#address_list>li:first-child')))
    # 选择收货地址
    # driver.find_element(By.CSS_SELECTOR, '#address_list>li:first-child').click()
    # time.sleep(3)
    # 选择货到付款
    driver.find_element(By.CSS_SELECTOR, '//*[text()="货到付款"]').click()
    # time.sleep(3)
    # 点击提交订单
    wait.until(element_click_is_success((By.LINK_TEXT, '提交订单')))
    # driver.find_element(By.LINK_TEXT, '提交订单').click()
    # time.sleep(3)
    # 断言--提示语

    # pytest.assume('订单状态刷新可能会延迟，如果您已付款成功，请勿重复支付!' in driver.page_source)
    flag_1 = wait.unit(pagesource_contains_text('订单状态刷新可能会延迟，如果您已付款成功，请勿重复支付!'))
    pytest.assume(flag_1)
    # 断言 --测试数据-- 交易号
    trade_sn = driver.find_element(By.TAG_NAME, 'b').text
    driver.find_element(By.LINK_TEXT, '查看订单').click()
    time.sleep(2)
    # 拼接订单号
    order_info = '订单编号' + trade_sn
    flag_2 = wait.unit(pagesource_contains_text(order_info))
    # 判断订单号信息是否在页面源码中
    # pytest.assume(order_info in driver.page_source)
    pytest.assume(flag_2)
def modify_birth(driver:webdriver):
    time.sleep(3)
    # 进入修改生日信息页面
    driver.get('http://www.mtxshop.com:3000/member/my-profile')
    # # js操作修改目标元素的属性
    js = '''document.getElementsByClassName('el-input__inner')[1].readOnly='';'''
    driver.execute_script(js)
    # modify_value = driver.find_element(By.XPATH, '//*[text()="生日"]/following-sibling::*//input')
    # js_value = 'arguments[0].readOnly="";'
    # driver.execute_script(js_value, modify_value)
    # 清空生日输入框
    driver.find_elements(By.CLASS_NAME, 'el-input__inner')[1].clear()
    # 输入目标日期
    driver.find_elements(By.CLASS_NAME, 'el-input__inner')[1].send_keys('1990-01-02')
    # 点击鼠标左键-关闭弹窗
    action = ActionChains(driver)
    action.click()
    # 保存资料
    # driver.find_element(By.XPATH, '//*[text()="保存资料"]').click()
    # js的点击
    save_el = driver.find_element(By.XPATH, '//*[text()="保存资料"]')
    js_click = 'arguments[0].click();'
    driver.execute_script(js_click, save_el)
    time.sleep(1)
    # 断言：提示语
    pytest.assume('修改成功!' in driver.page_source)
    # 断言：数据断言
    driver.refresh()    # 刷新
    time.sleep(3)
    # 获取页面实际的值
    actual_value = driver.find_elements(By.CLASS_NAME, 'el-input__inner')[1].get_attribute('value')
    pytest.assume(actual_value == '1990-01-02')

def upload_head(driver:WebDriver):
    time.sleep(3)
    driver.get('http://www.mtxshop.com:3000/member/my-profile')
    # 定位上传文件的input标签
    driver.find_element(By.CSS_SELECTOR, 'input[type=file]').send_keys('E:\learning\python\pycharm\project\wy3.jpg')
    time.sleep(2)
    # 点击上传弹窗的确定按钮
    driver.find_element(By.XPATH, '//*[text()="确 定"]').click()
    time.sleep(2)
    # 断言
    pytest.assume('上传成功，保存后生效' in driver.page_source)

def upload_head1(driver:WebDriver):
    time.sleep(3)
    driver.get('http://www.mtxshop.com:3000/member/my-profile')
    # 点击打开操作系统弹窗的元素
    driver.find_element(By.CSS_SELECTOR, 'div.el-upload--text').click()
    time.sleep(3)
    # 将图片路径复制到粘贴板
    pyperclip.copy('E:\learning\python\pycharm\project\wy3.jpg')
    # 采用键盘ctrl+V，将图片路径粘贴到选择文件的输入框中
    key_board = Controller()
    key_board.press(Key.ctrl.value)  # 按下ctrl键
    key_board.press('v')    # 按下v
    key_board.release(Key.ctrl.value)  # 释放ctrl
    key_board.release('v')  # 释放v
    # 模拟回车键完成上传
    key_board.press(Key.enter)  # 按下enter键
    key_board.release(Key.enter)    # 释放enter键
    time.sleep(2)
    # 点击上传弹窗的确定按钮
    driver.find_element(By.XPATH, '//*[text()="确 定"]').click()
    time.sleep(2)
    # 断言
    pytest.assume('上传成功，保存后生效' in driver.page_source)
    driver.find_element(By.XPATH, '//*[text()="保存资料"]').click()
    js = "window.scrollTo(0, 10000)"
    driver.execute_script(js)

if __name__ == '__main__':
    pass
    driver = webdriver.Chrome()  # 生产数据
    # 最大化
    driver.maximize_window()
    # 打开浏览器
    driver.get('http://www.mtxshop.com:3000/')
    # 登录
    login(driver)
    modify_birth(driver)
    # def click_is_success():
    #     try:
    #         driver.find_element(By.CSS_SELECTOR,'#address_list>li:first-child').click()
    #         return True
    #     except Exception as e:
    #         return False
    # wait = WebDriverWait(driver, 10)
    # wait.until(click_is_success)
    # 判断元素点击是否成功
    def click_is_scuccess(driver):
        try:
            driver.find_element(By.CSS_SELECTOR, '#address_list>li:first-child').click()
            return True
        except Exception as e:
            return False
    wait = WebDriverWait(driver, 10)
    wait.until(click_is_scuccess)   # 条件中是一个可以调用的方法，函数中只有一个参数