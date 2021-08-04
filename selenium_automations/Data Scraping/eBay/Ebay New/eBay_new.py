from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from time import sleep
import string

import csv
from os import path, removedirs

search_query = input("What do you want to Search  :  ")
which_page   = int(input("\nOn which Page do you want to start scraping  :  "))
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
location_loc = "//button[@class='x-flyout__button']"
go_loc       = "//input[@type='submit' and @value='Go']"
select_loc   = "//span[@class='select']/select"
radio_loc    = "//input[@name='location' and @data-value='Australia Only']"
items_page_loc = "//span[@id='nid-OwT-0']/button[@aria-expanded='false']"
items_100_loc  = "//a[@class='fake-menu-button__item']/span[contains(text(), '100')]"

location       = WaitW.until(EC.presence_of_element_located((By.XPATH, location_loc))).click()
select_country = WaitW.until(EC.presence_of_element_located((By.XPATH, select_loc)))
selectdd       = Select(select_country)
selectdd.select_by_visible_text("Australia - AUS")
go             = WaitW.until(EC.presence_of_element_located((By.XPATH, go_loc)))
go.click()
radio_btn      = WaitW.until(EC.presence_of_element_located((By.XPATH, radio_loc))).click()
# items_per_page = WaitW.until(EC.presence_of_element_located((By.XPATH, items_page_loc)))
# items_100      = WaitW.until(EC.presence_of_element_located((By.XPATH, items_100_loc))).click()

#///------------------------------------------------------------------------------------------------------///

current_url = driver.current_url

for page_no in range(which_page, which_page + pages_scrap):

    driver.get(current_url + '&_pgn=' + str(page_no))
    sleep(4)
    #Product_item_locators 
    title_loc          = "//h3[@class='s-item__title']"
    # item_condition_loc = "//span[@class='BOLD NEGATIVE']//ancestor::div[@class='s-item__info clearfix']/div[@class='s-item__subtitle']/span[@class='SECONDARY_INFO']"
    price_loc          = "//span[@class='s-item__price']"
    # sold_watchers_loc  = "//span[@class='BOLD NEGATIVE']"


    titles = WaitW.until(EC.presence_of_all_elements_located((By.XPATH, title_loc)))
    # item_conditions = WaitW.until(EC.presence_of_all_elements_located((By.XPATH, item_condition_loc)))
    prices          = WaitW.until(EC.presence_of_all_elements_located((By.XPATH, price_loc)))
    # sold_watchers  = WaitW.until(EC.presence_of_all_elements_located((By.XPATH, sold_watchers_loc)))

    for (title, price) in zip(titles, prices):
        my_title = title.text
        my_price = price.text
        my_price = my_price.replace('AU $', "")
        my_price = my_price.replace('to', '-')
        page_no = page_no

        file_name = search_query + "_eBay" + ".csv"
        field_names = ['TITLE', 'PRICE', 'PAGE-NO']

        my_dict = {
            "TITLE" : my_title,
            "PRICE" : my_price,
            "PAGE-NO" : page_no
        }

        extract_data(file_name, field_names, my_dict)
    
    print()
    print("Page-" + str(page_no) + " Scrapped.\n")

sleep(5)


driver.quit()


