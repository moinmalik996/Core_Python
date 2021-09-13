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

t=10

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get("https://bc.game/")
mywait = Wait(driver, t)

sleep(2)

close_loc = "//button[@class='close flex-center']"
close = mywait.until(EC.presence_of_element_located((By.XPATH, close_loc))).click()

sleep(2)

sign_in_loc = "//*[@id='header']/div/div/p"
sign_in = mywait.until(EC.presence_of_element_located((By.XPATH, sign_in_loc))).click()

user_name_loc  = "//input[@type='text']"
password_loc   = "//input[@type='password']"
login_btn_loc  = "//button[@class='sc-kEqXSa sc-dIsUp bAVzgZ jEEywD button button-big']"

sleep(2)

user_name   = mywait.until(EC.presence_of_element_located((By.XPATH, user_name_loc)))
user_name.send_keys("moinmalik996")

sleep(2)

password    = mywait.until(EC.presence_of_element_located((By.XPATH, password_loc)))
password.send_keys("m@l!k1122")

sleep(2)

login_btn   = mywait.until(EC.presence_of_element_located((By.XPATH, login_btn_loc)))
login_btn.click()


sleep(20)

