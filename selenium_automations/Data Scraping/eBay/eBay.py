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

search_query = input("What do you want to Search  :  ")
pages_scrap  = int(input("\nHow Many Pages Do You Want To Scrape  :  "))

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

#///-----------------------Extract FUnction------------------------------------------///

def extract_data(file_func, field_names_func, data):
    file_exist = path.exists(search_query+ "_eBay" + ".csv")
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

#///------------------------------END-------------------------------------------------///

driver.get("https://www.ebay.com.au/")
#time

t = 20
WaitW = Wait(driver, t)

#///-------------------------------SEARCH QUERY---------------------------------------///

search_bar_loc = "gh-ac"
search_btn_loc = "gh-btn"

search_bar = WaitW.until(EC.presence_of_element_located((By.ID, search_bar_loc)))
search_bar.send_keys(search_query)

search_btn = WaitW.until(EC.presence_of_element_located((By.ID, search_btn_loc)))
search_btn.click()

#///----------------------------------------------------------------------------------///

#Postal Code
location_loc = "x-flyout__button"
go_loc       = "//*[@id='s0-14-11-5-1[0]-36']/form/input"
go_loc_CSS   = "#s0-14-11-5-1\[0\]-36 > form > input"
select_loc   = "//span[@class='select']/select"

location       = WaitW.until(EC.presence_of_element_located((By.CLASS_NAME, location_loc))).click()
select_country = WaitW.until(EC.presence_of_element_located((By.XPATH, select_loc)))
selectdd       = Select(select_country)
selectdd.select_by_visible_text("Australia - AUS")
go             = WaitW.until(EC.presence_of_element_located((By.CSS_SELECTOR, go_loc_CSS)))
go.click()

#///------------------------------------------------------------------------------------------------------///

current_url = driver.current_url

for page_no in range(1, pages_scrap+1):

    driver.get(current_url + '&_pgn=' + str(page_no))

    #Product_item_locators 
    title_loc          = "//*[@id='srp-river-results']/ul/li/div/div/a/h3"
    item_condition_loc = "//*[@id='srp-river-results']/ul/li/div/div/div/span[text()='Brand new']"
    price_loc          = "//*[@id='srp-river-results']/ul/li/div/div[2]/div[3]/div[1]/span"
    sold_watchers_loc  = "//span[@class='BOLD NEGATIVE']"


    titles = WaitW.until(EC.presence_of_all_elements_located((By.XPATH, title_loc)))
    item_conditions = WaitW.until(EC.presence_of_all_elements_located((By.XPATH, item_condition_loc)))
    prices          = WaitW.until(EC.presence_of_all_elements_located((By.XPATH, price_loc)))
    sold_watchers  = WaitW.until(EC.presence_of_all_elements_located((By.XPATH, sold_watchers_loc)))

    for (title, item_condition, price, sold_watcher) in zip(titles, item_conditions, prices, sold_watchers):
        my_title = title.text
        my_item_condition = item_condition.text
        my_price = price.text
        my_price = my_price.replace('AU $', "")
        my_price = my_price.replace('to', '-')
        my_sold_watcher = sold_watcher.text
        page_no = page_no

        file_name = search_query + "_eBay" + ".csv"
        field_names = ['TITLE', 'ITEM-CONDITION', 'PRICE', 'SOLD / WATCHERS', 'PAGE-NO']

        my_dict = {
            "TITLE" : my_title,
            "ITEM-CONDITION": my_item_condition,
            "PRICE" : my_price,
            "SOLD / WATCHERS" : my_sold_watcher,
            "PAGE-NO" : page_no
        }

        extract_data(file_name, field_names, my_dict)
    
    print()
    print("Page-" + str(page_no) + " Scrapped.\n")

sleep(5)


driver.quit()


