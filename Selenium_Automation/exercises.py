from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime

exec_path = r"C:\Users\moinm\Desktop\Github\Python\Selenium_Automation\Drivers\chromedriver.exe"
wiki = r"https://www.wikipedia.org/"
google = r"https://www.google.com/"

driver = webdriver.Chrome(executable_path=exec_path)
driver.get(wiki)


# Now Locating Elements
sleep(3)
english_link = driver.find_element(By.ID, 'js-link-box-en')
english_link.click()

sleep(3)
search_bar = driver.find_element(By.NAME, 'search')
search_bar.send_keys('Software')
search_bar.submit()










