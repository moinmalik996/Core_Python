import csv
from os import path
from pprint import pprint
import urllib



from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep


total_crawled_products = 0
t = 10
CATEGORIES_MAPPING = dict()
SUB_CATEGORIES_MAPPING = dict()

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
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

args = {
    'f[price_range:max]': max_price, 
    'f[price_range:min]': min_price,
    'page': 1
    }

url = "{}?{}".format(SUB_CATEGORIES_MAPPING[choose_category]['url'], urllib.parse.urlencode(args))
driver.get(url)

products = Wait(driver, t).until(EC.presence_of_all_elements_located((By.XPATH, products_div_loc)))

# for product in products:

#     Wait(driver, t).until(EC.presence_of_all_elements_located((By.XPATH, products_div_loc)))


sleep(20)
driver.close()
driver.quit()


