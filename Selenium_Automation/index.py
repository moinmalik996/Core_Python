from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('C:\\Users\\moinm\\Desktop\\Github\\Core_Python_PyCharm\\Selenium_Automation\\Drivers\\chromedriver.exe')

driver.set_page_load_timeout("10")
driver.get("https://google.com")
driver.find_element_by_name('q').send_keys("Automatiom Step by Step")
driver.find_element_by_name('btnk').send_keys(Keys.ENTER)
time.sleep(4)
driver.quit()


