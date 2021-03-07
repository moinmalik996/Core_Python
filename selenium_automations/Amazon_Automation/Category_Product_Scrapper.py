"""  
Commands to install these packages.

pip install selenium==4.0.0.b1
pip install webdriver-manager
     
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from time import sleep


import csv
from os import path

total_crawled_products = 0

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://amazon.co.uk')
print(driver.title, " Session Started")

t = 5

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
    file_exist = path.exists("Product_Sheets/" + current_catagory[catagory_no-1] + ".csv")
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
    
    product_name_loc = "#zg-ordered-list > li > span > div > span > a > div"
    product_reviews_loc = "#zg-ordered-list > li > span > div > span > div.a-icon-row.a-spacing-none > a.a-size-small.a-link-normal"
    price_loc = "#zg-ordered-list > li > span > div > span > div.a-row > a > span"
    product_links_loc = "span.zg-item > a"
    
    print("Current URL is  :  ", cat_url)
    
    product_name    = Wait(driver, t).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, product_name_loc)))
    product_links   = Wait(driver, t).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, product_links_loc)))
    
    try:
        product_reviews = Wait(driver, t).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, product_reviews_loc)))
        product_price   = Wait(driver, t).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, price_loc)))
    except:
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        
    
    products_per_page = len(product_name)
    print("\nProducts found on this page", products_per_page)
    total_crawled_products += products_per_page
    
    for (product, review, price, links) in zip(product_name, product_reviews, product_price, product_links):  
        prt_name = product.text
        rvw = review.text
        prc_name = price.text
        prc_name = prc_name.replace('£', '')
        link_url = links.get_attribute("href")
        
        file = "Product_Sheets/" + current_catagory[catagory_no-1] + ".csv"
        field_names = ["NAME", "PRODUCT URL", "PRICE RANGE", "REVIEWS", "SUBCATAGORY"]
        
        my_dict = {
            "NAME" : prt_name,
            "PRODUCT URL": link_url,
            "PRICE RANGE" : prc_name,
            "REVIEWS" : rvw,
            "SUBCATAGORY" : sub_catagory_name
        }
        
        extract_data(file, field_names, my_dict)

    page_2 = Wait(driver, t).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li.a-last > a'))).click()
        
    product_name_loc = "#zg-ordered-list > li > span > div > span > a > div"
    product_reviews_loc = "#zg-ordered-list > li > span > div > span > div.a-icon-row.a-spacing-none > a.a-size-small.a-link-normal"
    price_loc = "#zg-ordered-list > li > span > div > span > div.a-row > a > span"
    product_links_loc = "span.zg-item > a"
        
    product_name    = Wait(driver, t).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, product_name_loc)))
    product_links   = Wait(driver, t).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, product_links_loc)))
    
    try:
        product_reviews = Wait(driver, t).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, product_reviews_loc)))
        product_price   = Wait(driver, t).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, price_loc)))
    except:
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    
    
    products_per_page = len(product_name)
    print("\nProducts found on this page 2 :", products_per_page)
    total_crawled_products += products_per_page
    
    for (product, review, price, links) in zip(product_name, product_reviews, product_price, product_links):  
        prt_name = product.text
        rvw = review.text
        prc_name = price.text
        prc_name = prc_name.replace('£', '')
        link_url = links.get_attribute("href")        
        file = current_catagory[catagory_no-1]+".csv"
        field_names = ["NAME", "PRODUCT URL", "PRICE RANGE", "REVIEWS", "SUBCATAGORY"]
        
        my_dict = {
            "NAME" : prt_name,
            "PRODUCT URL": link_url,
            "PRICE RANGE" : prc_name,
            "REVIEWS" : rvw,
            "SUBCATAGORY" : sub_catagory_name
        }
        
        extract_data(file, field_names, my_dict)                            
    
    sleep(5)
    
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    
print("Total Crawled Products  :  ", total_crawled_products) 