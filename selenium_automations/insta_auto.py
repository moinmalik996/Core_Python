"""
You need two packages to run the code.

1. Selenium - using the command  [ pip install selenium==4.0.0.a7  ]
2. WebDriver Manager - Automatically include the desired Webdriver for any browser  [ pip install webdriver-manager ]

What This Program does ?

-> Login to Instagram
-> Write a query in the search box
-> Extract all the suggestions as IDs and Tags
-> Store them in a List
-> Then print the list

"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

# For CSV File Operations
import csv
from os import path


#
def extract_data(file_func, field_names_func, data):
    file_exist = path.exists(r'C:\Users\moinm\PycharmProjects\Core_Python\selenium_automations\Boxing.csv')
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


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://instagram.com')

# Elements Locators
username_locator = "username"
password_locator = "password"
login_locator = "#loginForm > div > div:nth-child(3) > button"
notnow_locator = "#react-root > section > main > div > div > div > div > button"
notnow_locator_2 = "body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm"
search_locator = "input[placeholder='Search']"
ag_locator = "div.drKGC > div > a"

name_locator = "//h2"
posts_locator = "//*[@id='react-root']/section/main/div/header/section/ul/li[1]/span/span"
followers_locator = "//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/span"
following_locator = "//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a/span"

username = Wait(driver, 4).until(EC.presence_of_element_located((By.NAME, username_locator)))
username.send_keys("influencerhunter996")

password = Wait(driver, 4).until(EC.presence_of_element_located((By.NAME, password_locator)))
password.send_keys("!nfluencerhunter")

login = driver.find_element(By.CSS_SELECTOR, login_locator)
login.click()

not_now = Wait(driver, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR, notnow_locator)))
not_now.click()

not_now_2 = Wait(driver, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR, notnow_locator_2)))
not_now_2.click()

search = Wait(driver, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR, search_locator)))
search.send_keys("boxing")

auto_suggestions = Wait(driver, 4).until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, ag_locator)))

print("\nTotal Suggestions are  :  ", len(auto_suggestions), "\n")

# Extracting IDs and Hashtags Separately
for sugg in auto_suggestions:
    term = "explore"
    link = sugg.get_attribute('href')

    if term not in link:
        driver.execute_script("window.open('')")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(link)

        name = Wait(driver, 10).until(EC.presence_of_element_located((By.XPATH, name_locator)))
        posts = Wait(driver, 10).until(EC.presence_of_element_located((By.XPATH, posts_locator)))
        followers = Wait(driver, 10).until(EC.presence_of_element_located((By.XPATH, followers_locator)))
        following = Wait(driver, 10).until(EC.presence_of_element_located((By.XPATH, following_locator)))

        file = r"C:\Users\moinm\PycharmProjects\Core_Python\selenium_automations\Boxing.csv"
        field_names = ['NAME', 'POSTS', 'FOLLOWERS', 'FOLLOWING']
        my_dict = {
            'NAME': name.text,
            'POSTS': posts.text,
            'FOLLOWERS': followers.text,
            'FOLLOWING': following.text
        }

        extract_data(file, field_names, my_dict)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

#     item = sugg.get_attribute('href')
#     term = "explore"
#     if term in item:
#         explore.append(item)
#     else:
#         IDs.append(item)
#
# # Printing Explore URLS and Id URLS
# print("\nExplore URLs are  :  ")
# for exp in explore:
#     print(exp)
# print("\n\nID URLs are       :  ")
# for ids in IDs:
#     print(ids)
