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

mylist = ["uk.", "ca.", ""]
choose = int(input("Input 0 for UK 1 for CA and 2 for America :  "))
start_with = input("Enter A Character The Brand Start With    :  ")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

# Time
t = 2
    
driver.get('https://' + mylist[choose] + 'findthisbest.com/sellers/amazon')
print(driver.title, " Session Started")

# Categories
categories_link_loc = "//*[@id='content']/div/div/div/div/a"
categories_link     = Wait(driver, t).until(EC.presence_of_all_elements_located((By.XPATH, categories_link_loc)))
no_of_categories    = len(categories_link)
                        
category_url        = []
current_category    = []
                        
for i, catagory in zip(range(no_of_categories), categories_link):
    current_category.append(catagory.text)
    category_url.append(catagory.get_attribute("href"))
    print(i+1, ". ", catagory.text)

category_no = int(input("\n\nEnter catagory No. to go through particular catagory  :  "))
print("You Selected ", current_category[category_no - 1], ".")


cat_url = category_url[category_no - 1] + "/" + start_with
driver.get(cat_url)

nav_pages_loc = "//*[@id='content']/div[2]/div/div[2]/div/div[3]/nav/ul/li"
try:
    nav_pages     = Wait(driver, t).until(EC.presence_of_all_elements_located((By.XPATH, nav_pages_loc)))
except TimeoutException:
    pass

pages = len(nav_pages) - 2

for k in range(pages):
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(cat_url + "?page=" + str(k+1))

    # Locators
    sellers_loc   = "//*[@id='content']/div[2]/div/div[2]/div/div[2]/table/tbody/tr/td/a"
    sellers_link  = Wait(driver, t).until(EC.presence_of_all_elements_located((By.XPATH, sellers_loc)))        

    for link in sellers_link:
        link_url = link.get_attribute("href")
        driver.execute_script("window.open()")
        driver.switch_to.window(driver.window_handles[2])
        driver.get(link_url)
            
        #Locators
        seller_name_loc       = "//h1"
        seller_store_link_loc = "//*[@id='content']/div[2]/div/div[1]/div/div/div[2]/div[1]/a"
        company_name_loc      = "//span[text()='Company']/following::span"
        business_address_loc  = "//span[text()='Business Address']/following::span"
        contacts_loc          = "//span[text()='Contacts']/following::span"
        business_country_loc  = "//span[text()='Business Country']/following::div"
        reviews_loc           = "//*[@id='content']/div[2]/div/div[1]/div/div/div[1]/div/span[2]"
        
        def remove(mychar):
            remove_char = "()reviews"
            for char in remove_char:
                mychar = mychar.replace(char, "").strip()
            return mychar
            
        def myfunc(locator, exception_value):
            try:
                location = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, locator))).text
                return location
            except:
                return exception_value    
    
        seller_name      = myfunc(seller_name_loc, "No Name")
        company_name     = myfunc(company_name_loc, "No Company Name")    
        business_address = myfunc(business_address_loc, "No Business Address")
        business_country = myfunc(business_country_loc, "No Business Country")
        reviews          = myfunc(reviews_loc, 0)
        reviews          = remove(reviews)
        contacts         = myfunc(contacts_loc, 0)
        
        try:
            seller_store_link = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, seller_store_link_loc))).get_attribute("href")
        except:
            seller_store_link = "No Link"
            
        def extract_data(file_func, field_names_func, data):
            file_exist = path.exists("Sellers_" + current_category[category_no - 1] + ".csv")
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
                        
        file = "Sellers_" + current_category[category_no - 1] + ".csv"
        field_names = ["BRAND_NAME", "STORE_URL", "COMPANY_NAME", "COUNTRY", "BUSINESS_ADDRESS", "REVIEWS", "CONTACT"]
            
        my_dict = {
            "BRAND_NAME"        : seller_name,
            "STORE_URL"         : seller_store_link,
            "COMPANY_NAME"      : company_name,
            "COUNTRY"           : business_country,
            "BUSINESS_ADDRESS"  : business_address,
            "REVIEWS"           : reviews,
            "CONTACT"           : contacts
        }
                        
        extract_data(file, field_names, my_dict)
                
            
        driver.close()
        driver.switch_to.window(driver.window_handles[1])       
driver.close()
driver.switch_to.window(driver.window_handles[0])