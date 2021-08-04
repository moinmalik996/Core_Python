from sys import warnoptions
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

search_query = input("What do you want to Search  :  ")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get("https://www.canpages.ca/")

#time 
t = 20

search_bar_loc = "search-term-input"
location_loc   = "//div[@id='location-field-view']"

location   = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, location_loc)))
mylocation = location.text


search_bar = Wait(driver, t).until(EC.presence_of_element_located((By.ID, search_bar_loc)))
search_bar.send_keys(search_query)

sleep(10)


find_loc = "business-search-form-submit"
find_btn = Wait(driver, t).until(EC.presence_of_element_located((By.ID, find_loc))).click()


def extract_data(file_func, field_names_func, data):
    file_exist = path.exists("CanPages_" + search_query + ".csv")
    if file_exist:
        with open(file_func, 'a', newline='', encoding='utf-8') as myfile:
            file_writer = csv.DictWriter(myfile, fieldnames=field_names_func)
            file_writer.writerow(data)
            myfile.close()
    else:
        with open(file_func, 'w', newline='', encoding='utf-8') as myfile:
            file_writer = csv.DictWriter(myfile, fieldnames=field_names_func)
            file_writer.writeheader()
            file_writer.writerow(data)
            myfile.close()


name_loc           = "//a[@class='result__name']"
address_loc        = "//div[@class='result__address']"
phone_no_click_loc = "//span[@class='text']"
phone_num_loc      = "//span[@class='phone__number']"
total_results_loc  = "//h1[@class='results__summary']/strong[1]"

total_results = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, total_results_loc)))


total_results = total_results.text
t_r = total_results.replace(',', '')
print(t_r)
total_result       = int(t_r)
print('total_result\n\n')


item_no     = 1
current_url = driver.current_url
page_no     = 1


while(item_no <= total_result and page_no <= 10000):

    driver.get(current_url + "&p=" + str(page_no)) 
    print("\nData Extraction Started On Page _ ", page_no)

    names         = Wait(driver, t).until(EC.presence_of_all_elements_located((By.XPATH, name_loc)))
    addresses     = Wait(driver, t).until(EC.presence_of_all_elements_located((By.XPATH, address_loc)))
    phone_clicks  = Wait(driver, t).until(EC.presence_of_all_elements_located((By.XPATH, phone_no_click_loc)))
    phone_nums    = Wait(driver, t).until(EC.presence_of_all_elements_located((By.XPATH, phone_num_loc)))

    for(name, address, phone_click, phone_num) in zip(names, addresses, phone_clicks, phone_nums):
        phone_click.click()

        name_l = name.text
        address_l = address.text
        phone_no_l = phone_num.text

        


        file = "CanPages_" + search_query + ".csv"
        field_names = ["RECORD_NO", "NAME", "PHONE_NO", "AREA", "ADDRESS"]
            
        my_dict = {
            "RECORD_NO"     : item_no,
            "NAME"          : name_l,
            "PHONE_NO"      : phone_no_l,
            "AREA"          : mylocation,
            "ADDRESS"       : address_l,

        }
                        
        extract_data(file, field_names, my_dict)

        item_no += 1
    
    page_no += 1
    sleep(1)


sleep(10)


