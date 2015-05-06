#encoding: utf-8
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://sy.58.com/zhaozu/?PGTID=14281538140150.007925275512721375&ClickID=1')
print driver.title  # 把页面title 打印出来
driver.quit()