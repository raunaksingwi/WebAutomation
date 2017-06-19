from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#Enter your username and password below
USER_ID = "rsingwi"
PASSWORD = "IlovemymomdaD7"
FROM_STATION = "ngp"
TO_STATION = "cstm"
DATE_OF_JOURNEY = "21-06-2017"

driver = webdriver.Chrome()
driver.get("https://www.irctc.co.in/eticketing/loginHome.jsf")

#login page
userid = driver.find_element_by_name("j_username")
password = driver.find_element_by_name("j_password")
captcha = driver.find_element_by_name("j_captcha")
submit = driver.find_element_by_id("loginbutton")

userid.send_keys(USER_ID)
password.send_keys(PASSWORD)
captcha.send_keys(raw_input("Enter the captcha\n"))
submit.click()
#logged in

fromStation = driver.find_element_by_id("jpform:fromStation")
toStation = driver.find_element_by_id("jpform:toStation")
journeyDate = driver.find_element_by_id("jpform:journeyDateInputDate")
submit = driver.find_element_by_id("jpform:jpsubmit")
#quota = driver.find_element_by_xpath("//input[@value='TQ']")

fromStation.send_keys(FROM_STATION)
fromStation.send_keys(Keys.RETURN)
toStation.send_keys(TO_STATION)
toStation.send_keys(Keys.RETURN)
journeyDate.send_keys(DATE_OF_JOURNEY)
submit.click()
#quota.click()

duronto = driver.find_element_by_id("cllink-12290-SL-3")
duronto.click()