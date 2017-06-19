from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com")
elem = driver.find_element_by_name("q")
elem.send_keys("automation is cool")
elem.send_keys(Keys.RETURN)
driver.quit()