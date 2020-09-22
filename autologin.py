#!/usr/bin/env python
# @author : Pranav Agarwal
# Date: 22 September, 2020

from selenium import webdriver
driver = webdriver.Firefox()
username='enter your temp roll no.'
password='erp password'
website='http://app.cloudeducationerp.com/mrei'
driver.get(website)
user_box = driver.find_element_by_id("useriid")
user_box.send_keys(username)
pass_box = driver.find_element_by_id("actlpass")
pass_box.send_keys(password)
login = driver.find_element_by_id("psslogin")
login.submit()
