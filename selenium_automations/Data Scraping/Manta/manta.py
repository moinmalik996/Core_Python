from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from time import sleep
import string

import csv
from os import path, removedirs

t = 120

myquery = input("What do you want to search  :  ")
mylocation = input("Where do you want to search [ Country ]  :  ")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get("https://www.manta.com/")



search_bar_loc   = "//input[@name='search']"
location_bar_loc = "//input[@name='location']"

search_bar = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, search_bar_loc)))
search_bar.send_keys(myquery)

location_bar = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, location_bar_loc)))
location_bar.send_keys(mylocation)

location_suggestion_loc = "//ul/li/span[@class='small']"
location_suggestions = Wait(driver, t).until(EC.presence_of_all_elements_located((By.XPATH, location_suggestion_loc)))

for location in location_suggestions:
    print(location.text)



