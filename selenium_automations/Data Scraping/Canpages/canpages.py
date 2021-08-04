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
search_bar = Wait(driver, t).until(EC.presence_of_element_located((By.ID, search_bar_loc)))
search_bar.send_keys(search_query)

sleep(10)


find_loc = "business-search-form-submit"
find_btn = Wait(driver, t).until(EC.presence_of_element_located((By.ID, find_loc))).click()


def extract_data(file_func, field_names_func, data):
    file_exist = path.exists("CanPages/" + search_query +  + ".csv")
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


name_loc = "//a[@class='result__name']"
address_loc = "//div[@class='result__address']"
phone_no_click_loc = "//span[@class='text']"
phone_num_loc = "//span[@class='phone__number']"
next_link_loc = "//*[@id='results-page-paging']/ul/li[13]/a"

names = Wait(driver, t).until(EC.presence_of_all_elements_located((By.XPATH, name_loc)))
addresses = Wait(driver, t).until(EC.presence_of_all_elements_located((By.XPATH, address_loc)))
phone_clicks = Wait(driver, t).until(EC.presence_of_all_elements_located((By.XPATH, phone_no_click_loc)))
phone_nums = Wait(driver, t).until(EC.presence_of_all_elements_located((By.XPATH, phone_num_loc)))

next_link = Wait(driver, t).until(EC.presence_of_element_located(()))


while(True):

    for(name, address, phone_click, phone_num) in zip(names, addresses, phone_clicks, phone_nums):
        phone_click.click()

        print(name.text)
        print(address.text)
        print(phone_num.text)
        print()

    new_link = next_link.get_attribute("href")
    driver.execute_script("window.open()")
    driver.close()
    driver.switch_to.window(driver.window_handles[1])
    driver.get(new_link)





