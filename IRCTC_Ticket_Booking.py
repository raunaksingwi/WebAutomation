from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get("https://www.irctc.co.in/eticketing/loginHome.jsf")
CAPTCHA = raw_input("Enter the captcha :\n")

#Enter your username and password below
USER_ID = "rsingwi"
PASSWORD = "IlovemymomdaD7"
FROM_STATION = "ngp"
TO_STATION = "cstm"
DATE_OF_JOURNEY = "02-07-2017"
NAME = "Raunak Singwi"
AGE = 20
GENDER = "M" #Type exactly like 'M' or 'F'
BED_ROLL = 'Y' #Type 'y' or 'n'



#login page
userid = driver.find_element_by_name("j_username")
password = driver.find_element_by_name("j_password")
captcha = driver.find_element_by_name("j_captcha")
submit = driver.find_element_by_id("loginbutton")

userid.send_keys(USER_ID)
password.send_keys(PASSWORD)
captcha.send_keys(CAPTCHA)
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
driver.find_element_by_xpath(".//input[@type='radio' and @value='TQ']").click()
duronto = driver.find_element_by_id("cllink-12290-SL-3")
duronto.click()

Book_Now = driver.find_element_by_link_text("Book Now")
Book_Now.click()

passanger_name = driver.find_element_by_id("addPassengerForm:psdetail:0:p1296938642")
passanger_name.send_keys(NAME)

passanger_age = driver.find_element_by_id("addPassengerForm:psdetail:0:j_idt568")
passanger_age.send_keys(AGE)



if BED_ROLL == 'Y' or BED_ROLL == 'y':
	bed_roll = driver.find_element_by_id("addPassengerForm:psdetail:0:bedRollOpt")
	bed_roll.click()

#driver.find_element_by_id("validate").click()