"""
    pip install selenium==4.19.0
    pip install webdriver-manager==3.0.0
"""


import csv
import urllib
from os import path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException



 
def extract_data(file_name, data_heading, data):
    file_exist = path.exists(file_name)
    if file_exist:
        with open(file_name, 'a', newline='', encoding='utf-8') as myfile:
            file_writer = csv.DictWriter(myfile, fieldnames=data_heading, extrasaction='ignore')
            file_writer.writerow(data)
            myfile.close()
    else:
        with open(file_name, 'w', newline='', encoding='utf-8') as myfile:
            file_writer = csv.DictWriter(myfile, fieldnames=data_heading,  extrasaction='ignore')
            file_writer.writeheader()
            file_writer.writerow(data)
            myfile.close()


total_crawled_products = 0
t10 = 10
t5 = t10 - 5
CATEGORIES_MAPPING = dict()
SUB_CATEGORIES_MAPPING = dict()
PRODUCT_DATA = dict()

LATEST_DRIVER_URL = "https://storage.googleapis.com/chrome-for-testing-public/123.0.6312.122/win64/chromedriver-win64.zip"
driver_path = "chromedriver.exe"

driver = webdriver.Chrome(service=Service(executable_path=driver_path))
driver.maximize_window()
driver.get('https://www.amazon.com.au')


# cookie_acceptor_loc = "//input[@name='accept']"
# location_locator = "//a[@id='nav-global-location-popover-link']"
# postcode_locator = "//input[@class='GLUX_Full_Width a-declarative']"
# apply_locator = "//span[@id='GLUXZipUpdate']"
# city_select_box_locator = "//select[@id='GLUXPostalCodeWithCity_DropdownList']"


# postcode = "2199"
# main_catagories_loc = '/html/body/div/div/div/div/div/div/div/div/div/div/div/div/div/a'


# # Enter UK Postcode
# try:
#     cookie_acceptor = Wait(driver, t10).until(EC.presence_of_element_located((By.XPATH, cookie_acceptor_loc))).click()
# except:
#     pass

# location = Wait(driver, t10).until(EC.presence_of_element_located((By.XPATH, location_locator))).click()
# postcode = Wait(driver, t10).until(EC.presence_of_element_located((By.XPATH, postcode_locator))).send_keys(postcode)

# city = Wait(driver, t10).until(EC.presence_of_element_located((By.XPATH, city_select_box_locator)))
# city_select = Select(city)

sleep(10)
print("===========> Coming Here")
driver.get("https://www.amazon.com.au/deals?ref_=nav_cs_gb")


print("Now Coming here")
total_pages_locator = "//div[@id='dealsGridLinkAnchor']/div/div/div/ul/li[@class='a-disabled'][3]"
total_pages = Wait(driver, t10).until(EC.presence_of_element_located((By.XPATH, total_pages_locator)))

# print('------>', total_pages.text)
for i in range(0, int(total_pages.text)):

    print('===========> coming here')
    sleep(2)
    data_divs_locator = "//div[@id='grid-main-container']/div[3]/div/div"
    data_divs = Wait(driver, t10).until(EC.presence_of_all_elements_located((By.XPATH, data_divs_locator)))

    for ele in data_divs:
        
        try:
            title = ele.find_element(By.XPATH, ".//div/div/div/a/div").text
            link = ele.find_element(By.XPATH, ".//div/div/div/a").get_attribute('href')
        except:
            title = ""
            link = ""
            
        print(title.text)
        print(link.get_attribute('href'))

        data = {
            'PRODUCT': title.text,
            'URL': link.get_attribute('href') 
        }

        file_name = "PrimeDeals.csv"
        header = [
            'PRODUCT',
            'URL'
        ]
        extract_data(file_name, header, data)

    next_page_locator = "//div[@id='dealsGridLinkAnchor']/div/div/div/ul/li[@class='a-last']"
    next_page = Wait(driver, t10).until(EC.presence_of_element_located((By.XPATH, next_page_locator)))
    next_page.click()


sleep(10)


# driver.quit()



