from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

import csv
from os import path






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

product_name_loc = "//div[@class='p13n-sc-truncate-desktop-type2 p13n-sc-truncated']"
product_reviews_loc = "//a[@class='a-size-small a-link-normal']"
price_loc = "//span[@class='a-size-base a-color-price']"

page_2_loc = '//*[@id="zg-center-div"]/div[2]/div/ul/li[3]/a'

 # Enter UK Postcode
location = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, location_locator))).click()
postcode = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, postcode_locator))).send_keys(uk_postcode)
apply    = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, apply_locator))).click()

# Go to Best Sellers
sleep(5)
driver.get('https://www.amazon.co.uk/gp/bestsellers/?ref_=nav_cs_bestsellers')
main_catagory = "Sports-Outdoors"
main_catagory_url = "https://www.amazon.co.uk/Best-Sellers-"+main_catagory+"/zgbs/sports/ref=zg_bs_nav_0"
driver.get(main_catagory_url)

sub_catagory = Wait(driver, t).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, sub_catagories_loc)))

def extract_data(file_func, field_names_func, data):
    file_exist = path.exists("Selenium_Automations\\"+main_catagory+".csv")
    if file_exist:
        with open(file_func, 'a', newline='') as myfile:
            file_writer = csv.DictWriter(myfile, fieldnames=field_names_func)
            file_writer.writerow(data)
            myfile.close()
    else:
        with open(file_func, 'w', newline='') as myfile:
            file_writer = csv.DictWriter(myfile, fieldnames=field_names_func)
            file_writer.writeheader()
            file_writer.writerow(data)
            myfile.close()

for catagory in sub_catagory:
    catagory_name = catagory.text
    cat_url = catagory.get_attribute('href')
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(cat_url)
    
    print("Current URL is  :  ", cat_url)
    
    product_name    = Wait(driver, t).until(EC.presence_of_all_elements_located((By.XPATH, product_name_loc)))
    product_reviews = Wait(driver, t).until(EC.presence_of_all_elements_located((By.XPATH, product_reviews_loc)))
    product_price   = Wait(driver, t).until(EC.presence_of_all_elements_located((By.XPATH, price_loc)))
    
    products_per_page = len(product_name)
    
    print("\nProducts found on this page", products_per_page)
    for (product, review, price) in zip(product_name, product_reviews, product_price):
        prt_name = product.text
        rvw = review.text
        prc_name = price.text
        
        file = "Selenium_Automations\\"+main_catagory+".csv"
        field_names = ["NAME", "PRICE RANGE", "REVIEWS", "SUBCATAGORY"]
        
        my_dict = {
            "NAME" : prt_name,
            "PRICE RANGE" : prc_name,
            "REVIEWS" : rvw,
            "SUBCATAGORY" : catagory_name
        }
        
        extract_data(file, field_names, my_dict)
        
    
    sleep(5)
    
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    
    
    
    
    
    






