from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from time import sleep

import csv
from os import path

mylist = ["uk.", "ca.", ""]
choose = int(input("Input 0 for UK 1 for CA and 2 for America :  "))

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

# Time
t = 10

for page in range(1, 10):
    
    driver.get('https://' + mylist[choose] + 'findthisbest.com/sellers/amazon?page=' + str(page))
    print(driver.title, " Session Started")

    # Locators
    sellers_link_loc = "tr > td > a"
    sellers_link     = Wait(driver, t).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, sellers_link_loc)))

    for link in sellers_link:
        link_url = link.get_attribute("href")
        driver.execute_script("window.open()")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(link_url)
        
        #Locators
        seller_name_loc              = "//h1"
        seller_store_link_loc = "//*[@id='content']/div[2]/div/div[1]/div/div/div[2]/div[1]/a"
        company_name_loc      = "//span[text()='Company']/following::span"
        business_address_loc  = "//span[text()='Business Address']/following::span"
        contacts_loc          = "//span[text()='Contacts']/following::span"
        
        seller_name          = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, seller_name_loc))).text
        seller_store_link    = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, seller_store_link_loc))).get_attribute("href")
        company_name         = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, company_name_loc))).text
        
        try:
            contacts         = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, contacts_loc))).text
        except TimeoutException:
            contacts    = 0
            
        try:
            business_address = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, business_address_loc))).text
        except:
            business_address = "No Business Address"
        
        
        def extract_data(file_func, field_names_func, data):
            file_exist = path.exists("Sellers_" + mylist[choose] + ".csv")
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
                    
        file = "Sellers_" + mylist[choose] + ".csv"
        field_names = ["BRAND_NAME", "STORE_URL", "COMPANY_NAME", "BUSINESS_ADDRESS", "CONTACT"]
        
        my_dict = {
            "BRAND_NAME"        : seller_name,
            "STORE_URL"         : seller_store_link,
            "COMPANY_NAME"      : company_name,
            "BUSINESS_ADDRESS"  : business_address,
            "CONTACT"           : contacts
        }
                    
        extract_data(file, field_names, my_dict)
            
        
        driver.close()
        driver.switch_to.window(driver.window_handles[0])




