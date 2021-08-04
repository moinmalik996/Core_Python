from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get("https://facebook.com")

link_locator = '//a[text()="Create New Account"]'
create_account = Wait(driver, 5).until(EC.presence_of_element_located((By.XPATH, link_locator))).click()

sleep(3)

# Identify Select Element
month = Wait(driver, 5).until(EC.presence_of_element_located((By.ID, "month")))

# create Select Object with Select class
monthdd = Select(month)

# Check the Default Selected Option 
first_item = monthdd.first_selected_option
assert "Jan" == first_item.text

# select by Index
monthdd.select_by_index(3)  # It will select April

sleep(3)

# Select by Value
monthdd.select_by_value("3") # It will select March

sleep(3)

# Select by Visible_Text
monthdd.select_by_visible_text("Aug") # It will select August

ddlist = monthdd.options

for item in ddlist:
    print(item.text)
    if item.text == "Nov":
        item.click()





sleep(10)
driver.quit()









