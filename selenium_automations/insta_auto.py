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
auto_suggestions_locator = "div.drKGC > div > a"


username = Wait(driver, 4).until(EC.presence_of_element_located((By.NAME, username_locator)))
username.send_keys("your_username")

password = Wait(driver, 4).until(EC.presence_of_element_located((By.NAME, password_locator)))
password.send_keys("your_password")

login = driver.find_element(By.CSS_SELECTOR, login_locator)
login.click()

not_now = Wait(driver, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR, notnow_locator)))
not_now.click()

not_now_2 = Wait(driver, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR, notnow_locator_2)))
not_now_2.click()

search = Wait(driver, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR, search_locator)))
search.send_keys("boxing")

auto_suggestions = Wait(driver, 4).until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, auto_suggestions_locator)))


print("\nTotal Suggestions are  :  ", len(auto_suggestions), "\n")

explore = []
IDs = []

# Extracting IDs and Hashtags Separately
for sugg in auto_suggestions:
    item = sugg.get_attribute('href')
    term = "explore"
    if term in item:
        explore.append(item)
    else:
        IDs.append(item)

# Printing Explore URLS and Id URLS
print("\nExplore URLs are  :  ")
for exp in explore:
    print(exp)
print("\n\nID URLs are       :  ")
for ids in IDs:
    print(ids)




