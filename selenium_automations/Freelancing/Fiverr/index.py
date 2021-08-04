from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from time import sleep
import string

import csv
from os import path, removedirs

# search_query = input("What do you want to Search  :  ")
# pages_scrap  = int(input("\nHow Many Pages Do You Want To Scrape  :  "))

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

t = 20
WaitW = Wait(driver, t)




driver.get("https://loyverse.com/en/login")

email_loc  = "mat-input-0"
passw_loc  = "mat-input-1"
submit_loc = "sforg-submit"

email = WaitW.until(EC.presence_of_element_located((By.ID, email_loc)))
email.send_keys("moin.malik996@gmail.com")

sleep(4)

passw = WaitW.until(EC.presence_of_element_located((By.ID, passw_loc)))
passw.send_keys("malik1122")

sleep(4)

login = WaitW.until(EC.presence_of_element_located((By.ID, submit_loc))).click()



sleep(10)
