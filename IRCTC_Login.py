from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Enter your username and password below
User_ID = "rsingwi"
Password = "IlovemymomdaD7"

driver = webdriver.Chrome()
driver.get("https://www.irctc.co.in/eticketing/loginHome.jsf")
userid = driver.find_element_by_name("j_username")
password = driver.find_element_by_name("j_password")
captcha = driver.find_element_by_name("j_captcha")
submit = driver.find_element_by_id("loginbutton")

userid.send_keys(User_ID)
password.send_keys(Password)
captcha.send_keys(raw_input("Enter the captcha\n"))

submit.click()