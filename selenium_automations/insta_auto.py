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
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from instaloader import Instaloader, Profile


# For CSV File Operations
import csv
from os import path


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


# Login Credentials
login_id = 'influencerhunter996'
login_pass = '!nfluencerhunter'

# Enter something you want to search in IG Search Bar
search_term = input("Enter a Niche you want to Search   :   ")

headless1 = webdriver.FirefoxOptions()
headless1.headless = True
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.maximize_window()
driver.get('https://instagram.com')
print(driver.title, " Session Started")

# Elements Locators
username_locator = "username"
password_locator = "password"
login_locator = "#loginForm > div > div:nth-child(3) > button"
notnow_locator = "#react-root > section > main > div > div > div > div > button"
notnow_locator_2 = "body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm"
search_locator = "input[placeholder='Search']"
ag_locator = "//span[@class='Ap253']"

locator_wait = 5

# Filling Form and Log In
username = Wait(driver, locator_wait).until(EC.presence_of_element_located((By.NAME, username_locator)))
username.send_keys(login_id)

password = Wait(driver, locator_wait).until(EC.presence_of_element_located((By.NAME, password_locator)))
password.send_keys(login_pass)

login = driver.find_element(By.CSS_SELECTOR, login_locator)
login.click()

not_now = Wait(driver, locator_wait).until(EC.presence_of_element_located((By.CSS_SELECTOR, notnow_locator)))
not_now.click()

not_now_2 = Wait(driver, locator_wait).until(EC.presence_of_element_located((By.CSS_SELECTOR, notnow_locator_2)))
not_now_2.click()

# Enter Query in Search Bar
search = Wait(driver, locator_wait).until(EC.presence_of_element_located((By.CSS_SELECTOR, search_locator)))
search.send_keys(search_term)

# Autosuggestions
auto_suggestions = Wait(driver, locator_wait).until(EC.visibility_of_any_elements_located((By.XPATH, ag_locator)))

print("\nTotal Suggestions are  :  ", len(auto_suggestions), "\n")

loader = Instaloader()
loader.login(login_id, login_pass)

# Extracting IDs and Hashtags Separately
for sugg in auto_suggestions:
    suggestion = sugg.text
    term = "#"
    if term not in suggestion:
        print(suggestion)
        target_profile = suggestion

        profile = Profile.from_username(loader.context, target_profile)

        followers = profile.followers
        following = profile.followees
        total_num_likes = 0
        total_num_comments = 0
        total_num_posts = 0

        for post in profile.get_posts():
            total_num_likes += post.likes
            total_num_comments += post.comments
            total_num_posts += 1

        engagement_rate = float(total_num_likes + total_num_comments) / (followers * total_num_posts)

        file = r"C:\Users\moinm\PycharmProjects\Core_Python\selenium_automations\Boxing.csv"
        field_names = ['NAME', 'POSTS', 'FOLLOWERS', 'FOLLOWING', 'Engagement_Rate']
        my_dict = {
            'NAME': suggestion,
            'POSTS': total_num_posts,
            'FOLLOWERS': followers,
            'FOLLOWING': following,
            'Engagement_Rate': engagement_rate
        }
        extract_data(file, field_names, my_dict)
    else:
        print("Its a Hashtag")
