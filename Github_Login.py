from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Safari()
driver.get("https://github.com/login")
User_ID = "raunaksingwi7@gmail.com"
Password = "#importHacker.7"

userid = driver.find_element_by_name("login")
password = driver.find_element_by_name("password")
login = driver.find_element_by_name("commit")

userid.send_keys(User_ID)
password.send_keys(Password)
login.click()
raw_input()
driver.quit()