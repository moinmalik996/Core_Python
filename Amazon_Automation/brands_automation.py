from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from time import sleep

import csv
from os import path

total_crawled_products = 0

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://amazon.co.uk')
print(driver.title, " Session Started")

t = 10

location_locator = "//a[@id='nav-global-location-popover-link']"
postcode_locator = "//input[@class='GLUX_Full_Width a-declarative']"
apply_locator = "//span[@id='GLUXZipUpdate']"

uk_postcode = "WC2N 5DU"
sub_catagories_loc = 'ul > Ul > li > a'

 # Enter UK Postcode
location = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, location_locator))).click()
postcode = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, postcode_locator))).send_keys(uk_postcode)
apply    = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, apply_locator))).click()

# Go to Best Sellers
sleep(5)
driver.get('https://www.amazon.co.uk/gp/bestsellers/?ref_=nav_cs_bestsellers')
main_catagories = Wait(driver, t).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, sub_catagories_loc)))
no_of_catagories = len(main_catagories)

catagory_url = []
current_catagory = []

print("\n\nThere are total ",no_of_catagories, " catagories as follows : \n\n")

for i, catagory in zip(range(no_of_catagories), main_catagories):
    current_catagory.append(catagory.text)
    catagory_url.append(catagory.get_attribute("href"))
    print(i+1, ". ", catagory.text)

catagory_no = int(input("\n\nEnter catagory No. to go through particular catagory  :  "))
print("You Selected ", current_catagory[catagory_no - 1], ".")

driver.get(catagory_url[catagory_no - 1])

sub_catagories = Wait(driver, t).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, sub_catagories_loc)))

def extract_data(file_func, field_names_func, data):
    file_exist = path.exists(current_catagory[catagory_no-1]+".csv")
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

for catagory in sub_catagories:
    sub_catagory_name = catagory.text
    cat_url = catagory.get_attribute("href")
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(cat_url)
    
    
    product_links_loc = "span.zg-item > a"
    
    print("Current Category URL is  :  ", cat_url)
    
    ignored_except = (NoSuchElementException, StaleElementReferenceException)
    
    product_links   = Wait(driver, t).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, product_links_loc)))
    
    products_per_page = len(product_links)
    print("\nProducts found on this page", products_per_page)
    total_crawled_products += products_per_page
    
    for product in product_links:  
        product_url = product.get_attribute("href")
        driver.execute_script("window.open()")
        driver.switch_to.window(driver.window_handles[2])
        driver.get(product_url)
        
        seller_profile_id_loc = "sellerProfileTriggerId"
        seller_profile_id = Wait(driver, t).until(EC.presence_of_element_located((By.ID, seller_profile_id_loc))).click()
        
        business_name_loc        = "//*[@id='seller-profile-container']/div[2]/div/ul/li[1]/span"
        business_type_loc        = "//*[@id='seller-profile-container']/div[2]/div/ul/li[2]/span"
        trade_register_no_loc    = "//*[@id='seller-profile-container']/div[2]/div/ul/li[3]/span"
        vat_number_loc           = "//*[@id='seller-profile-container']/div[2]/div/ul/li[4]/span"
        business_address_loc     = "//*[@id='seller-profile-container']/div[2]/div/ul/li[5]/span/ul/li"
        
        business_name     = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, business_name_loc)))
        business_type     = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, business_type_loc)))
        trade_register_no = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, trade_register_no_loc)))
        vat_number        = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, vat_number_loc)))
        business_address  = Wait(driver, t).until(EC.presence_of_all_elements_located((By.XPATH, business_address_loc)))
        
        for address in business_address:
            print(address.text)
        
        
        driver.close()
        driver.switch_to.window(driver.window_handles[1])
        
    
    
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    
print("Total Crawled Products  :  ", total_crawled_products) 
