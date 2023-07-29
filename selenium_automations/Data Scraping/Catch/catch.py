import csv
import urllib
from os import path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException

from webdriver_manager.chrome import ChromeDriverManager

def extract_data(file_name, data_heading, data):
    file_exist = path.exists(file_name)
    if file_exist:
        with open(file_name, 'a', newline='', encoding='utf-8') as myfile:
            file_writer = csv.DictWriter(myfile, fieldnames=data_heading, extrasaction='ignore')
            file_writer.writerow(data)
            myfile.close()
    else:
        with open(file_name, 'w', newline='', encoding='utf-8') as myfile:
            file_writer = csv.DictWriter(myfile, fieldnames=data_heading,  extrasaction='ignore')
            file_writer.writeheader()
            file_writer.writerow(data)
            myfile.close()


total_crawled_products = 0
t = 10
t5 = t - 8
CATEGORIES_MAPPING = dict()
SUB_CATEGORIES_MAPPING = dict()
PRODUCT_DATA = dict()

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(version='114.0.5735.90').install()))
driver.maximize_window()
driver.get('https://www.catch.com.au')

def hover_it(element):
    hover_on = ActionChains(driver).move_to_element(element)
    return hover_on.perform()



# locators
hover_locator = '//div[@id="menu-bar-item-0"]'
all_categories_loc = '//ul[@class="css-mg94dl e144sfsb0"]'
category_link_loc = all_categories_loc + "//a[@class='css-1lu8pzx']"
category_name_loc = category_link_loc + "//div[@class='css-1u0783d']"
sub_categories_loc = "//ul[@class='category-visualiser__subcategories-list']//li//a[@class='category-visualiser__subcategory-link']"

min_price_loc = "//label[@id='price-slider-min-value']/input"
min_div_toggle = "//div[@id='f[price_range]']"
max_price_loc = "//label[@id='price-slider-max-value']/input"

products_div_loc = "//div[@class='css-wr32q5']/div"


hovered_element =  Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, hover_locator)))
hover_it(hovered_element)

categories_container =  Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, all_categories_loc)))
category_links =  Wait(driver, t).until(EC.presence_of_all_elements_located((By.XPATH, category_link_loc)))
category_names = Wait(driver, t).until(EC.presence_of_all_elements_located((By.XPATH, category_name_loc)))

for index, (link , name) in enumerate(zip(category_links, category_names)):

    CATEGORIES_MAPPING[index] = {
        'url': link.get_attribute('href'),
        'name': name.text,
    }

for key, value in CATEGORIES_MAPPING.items():
    print(key , '---------', value['name'])


choose_category = int(input('Choose a category with a number : '))

driver.get(CATEGORIES_MAPPING[choose_category]['url'])
PRODUCT_DATA['CATEGORY'] = CATEGORIES_MAPPING[choose_category]['name']
PRODUCT_DATA['CATEGORY URL'] = CATEGORIES_MAPPING[choose_category]['url']


sub_categories = Wait(driver, t).until(EC.presence_of_all_elements_located((By.XPATH, sub_categories_loc)))

for index, sub in enumerate(sub_categories):

    SUB_CATEGORIES_MAPPING[index] = {
        'name': sub.text,
        'url': sub.get_attribute('href')
    }

for idx, (key, value) in enumerate(SUB_CATEGORIES_MAPPING.items()):
    
    print(idx, '----------', SUB_CATEGORIES_MAPPING[idx]['name'])

choose_sub_category = int(input("CHoose a subcategory : "))
min_price = int(input('Choose a minimum price : '))
max_price = int(input('Choose a maximum price : '))
free_delivery = input('Only include free delivery (Y / N) : ')

PRODUCT_DATA['SUB CATEGORY'] = SUB_CATEGORIES_MAPPING[choose_sub_category]['name']
PRODUCT_DATA['SUB CATEGORY URL'] = SUB_CATEGORIES_MAPPING[choose_sub_category]['url']




for i in range(1, 100):  # a hard coded loop , should be dynamic 

    args = {
    'f[price_range:max]': max_price,
    'f[price_range:min]': min_price,
    'page': i
    }

    if free_delivery == 'Y':
        args['f[delivery]'] = 'free'


    url = "{}?{}".format(SUB_CATEGORIES_MAPPING[choose_sub_category]['url'], urllib.parse.urlencode(args))
    driver.get(url)

    products = Wait(driver, t).until(EC.presence_of_all_elements_located((By.XPATH, products_div_loc)))

    for idx in range(1, len(products) + 1):

        base_xpath = "//div[@class='css-wr32q5']"
        product_xpath = "{}/div[{}]/div/div[2]/div[1]/div[1]/span/h2/a".format(base_xpath, idx)
        brand_xpath = "{}/div[{}]/div/div[2]/div/div[2]/span/a".format(base_xpath, idx)
        old_price_xpath = "{}/div[{}]/div/div[2]/a/div/div[2]/div/div[1]/div/span".format(base_xpath, idx)
        price_xpath_1 = "{}/div[{}]/div/div[2]/a/div/div[2]/div/div[2]/div/span[2]".format(base_xpath, idx)
        price_xpath_2 = "{}/div[{}]/div/div[2]/a/div/div/div/div/div/span[2]".format(base_xpath, idx)

        product = Wait(driver, t5).until(EC.presence_of_element_located((By.XPATH, product_xpath)))
        try:
            brand = Wait(driver, t5).until(EC.presence_of_element_located((By.XPATH, brand_xpath)))
        except TimeoutException:
            brand = None

        product_name = product.get_attribute('text')
        product_url = product.get_attribute('href')
        brand_name = brand.get_attribute('text') if isinstance(brand, WebElement) else None
        brand_url = brand.get_attribute('href') if isinstance(brand, WebElement) else None

        try:
            price = Wait(driver, t5).until(EC.presence_of_element_located((By.XPATH, price_xpath_1)))
            old_price = Wait(driver, t5).until(EC.presence_of_element_located((By.XPATH, old_price_xpath)))
        except TimeoutException:
            price = Wait(driver, t5).until(EC.presence_of_element_located((By.XPATH, price_xpath_2)))
            old_price = None
        finally:
            pass

        
        product_price = price.text if isinstance(price, WebElement) else "Not Found"
        product_old_price = old_price.text if old_price is not None else 0




        data_header = ['CATEGORY', 
                    'CATEGORY URL', 
                    'SUB CATEGORY', 
                    'SUB CATEGORY URL', 
                    'PRODUCT NAME', 
                    'PRODUCT URL', 
                    'PRICE', 
                    'OLD PRICE', 
                    'BRAND NAME', 
                    'BRAND URL',
                    'PAGE NO'
                    ]
        
        PRODUCT_DATA['PRODUCT NAME'] = product_name
        PRODUCT_DATA['PRODUCT URL'] = product_url
        PRODUCT_DATA['PRICE'] = product_price
        PRODUCT_DATA['OLD PRICE'] = product_old_price
        PRODUCT_DATA['BRAND NAME'] = brand_name
        PRODUCT_DATA['BRAND URL'] = brand_url
        PRODUCT_DATA['PAGE NO'] = i

        file = "{}-{}.{}".format(PRODUCT_DATA['CATEGORY'], PRODUCT_DATA['SUB CATEGORY'], 'csv')

        extract_data(file, data_header, PRODUCT_DATA)


sleep(20)
driver.close()
driver.quit()


