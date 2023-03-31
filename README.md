# selenium_frame
1.selenium 八种定位方式
```driver.find_element_by_name('wd') # 返回值是元素
driver.find_element_by_id('id属性对应的值')
driver.find_element_by_class_name('class属性对应的值')
driver.find_element_by_tag_name('标签的名字') # 通过标签来定位
driver.find_element_by_link_text('a标签中包裹的文字进行定位') # 完全匹配
driver.find_element_by_partial_link_text('a标签中包裹的部分文字进行定位') # 包含关系匹配
### 如下两个表达式比较万能，常用
driver.find_element_by_xpath(xpath表达式)
driver.find_element_by_css_selector(css表达式)
```
新版本元素定位方法：
```
# id
driver.find_element(By.ID, "username")
# name
driver.find_element(By.NAME, "keyword")
# class name，class属性有多个值的话，可以只写一个值，用.
driver.find_element(By.CLASS_NAME, "login_btn")
# tag_name
driver.find_element(By.TAG_NAME, "select")
# link_text
driver.find_element(By.LINK_TEXT, "进入商城购物")
# partial_link_text
driver.find_element(By.PARTIAL_LINK_TEXT, "人资")
# xpath
driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[3]/div/div[1]/a/img")
# css_selector
driver.find_element(By.CSS_SELECTOR, '[value="1"]')
```

2.案例1：python中操作js代码（修改生日），js定位元素的语法：
```
通过id获取 (getElementById)
通过name属性(getElementsByName)
通过标签名(getElementsByTagName)
通过类名(getElementsByClassName)
# 以下两种方法适用范围更广
通过选择器获取一个元素(querySelector)
通过选择器获取一组元素(querySelectorAll)
```
3.selenium模块引用js脚本的语法

4.案例2：修改头像

5.智能等待（显示等待和隐式等待），显示等待的封装

6.iframe切换

7.alert截图

8.键盘操作、鼠标操作、select操作
