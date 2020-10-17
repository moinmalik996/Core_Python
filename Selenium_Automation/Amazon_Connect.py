from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd


# Change this to your own chromedriver path!
webdriver = webdriver.Chrome('C:\\Users\\moinm\\Desktop\\Github\\Core_Python_PyCharm\\Selenium_Automation\\Drivers\\chromedriver.exe') 
# webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)

webdriver.get('https://voice-foundry.awsapps.com/connect/login')
sleep(3)

username = webdriver.find_element_by_id('wdc_username')
username.send_keys('mohsin.malik')
password = webdriver.find_element_by_id('wdc_password')
password.send_keys('Welcome1')

sleep(3)

login = webdriver.find_element_by_id('wdc_login_button')
login.click()

sleep(3)

webdriver.get('https://voice-foundry.awsapps.com/connect/ctr/')

sleep(3)

from_date = webdriver.find_element_by_class_name('c-m-4 > span')
from_date.click()

date = webdriver.find_element_by_css_selector('datepicker-00K-5023-4 > button')
date.click()

for x in 
    contact_ids = webdriver.find_element_by_xpath('//*[@id="angularContainer"]/div[3]/div[1]/div/div/div[1]/table/tbody/tr[1]/td[1]')

