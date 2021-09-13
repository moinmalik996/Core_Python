"""  
Commands to install these packages.


pip install selenium==4.0.0.b1
pip install webdriver-manager

"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from time import sleep


import csv
from os import path

total_crawled_products = 0

query = input("What do you want to search in Amazon :  ")

def extract_data(file_func, field_names_func, data):
    file_exist = path.exists(query + ".csv")
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



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://amazon.com')
print(driver.title, " Session Started")

t = 5
cookie_acceptor_loc = "//input[@id='sp-cc-accept']"
location_locator = "//a[@id='nav-global-location-popover-link']"
postcode_locator = "//input[@id='GLUXZipUpdateInput']"
apply_locator = "//*[@id='GLUXZipUpdate']/span/input"

postcode = "10001"
sub_catagories_loc = 'ul > Ul > li > a'


# Enter UK Postcode
try:
    cookie_acceptor = Wait(driver, t ).until(EC.presence_of_element_located((By.XPATH, cookie_acceptor_loc))).click()
except:
    pass

location = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, location_locator))).click()
postcode = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, postcode_locator))).send_keys(postcode)
apply    = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, apply_locator))).click()

sleep(3)

# continue_loc = "/html/body/div[5]/div/div/div[2]/span/span/input"
# continue_l   = Wait(driver, t).until(EC.presence_of_element_located(By.XPATH, continue_loc)).click()


search_box_loc    = "//input[@id='twotabsearchtextbox']"
search_submit_loc = "//input[@id='nav-search-submit-button']"

search_box = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, search_box_loc)))
search_box.send_keys(query)
search_submit = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, search_submit_loc)))
search_submit.click()



ratings_loc = "//li[@id='p_72/1248915011']"
ratings = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, ratings_loc))).click()

current_url = driver.current_url

for page in range(1, 30):
    driver.get(current_url + "&page=" + str(page))


    name_loc    = "//span[@class='a-size-base-plus a-color-base a-text-normal']"
    reviews_loc = "//span[@class='a-size-base']"
    links_loc = "//a[@class='a-link-normal a-text-normal']"

    name = Wait(driver, t).until(EC.presence_of_all_elements_located((By.XPATH, name_loc)))
    reviews = Wait(driver, t).until(EC.presence_of_all_elements_located((By.XPATH, reviews_loc)))
    links = Wait(driver, t).until(EC.presence_of_all_elements_located((By.XPATH, links_loc)))

    for (name_item, reviews_item, links_item) in zip(name, reviews, links):
        name_a = name_item.text
        reviews_a =reviews_item.text
        url = links_item.get_attribute("href")

        file = query + ".csv"
        field_names = ["NAME", "PRODUCT URL", "REVIEWS"]

        my_dict = {
            "NAME" : name_a,
            "PRODUCT URL": url,
            "REVIEWS" : reviews_a
        }

        extract_data(file, field_names, my_dict)


sleep(5)
