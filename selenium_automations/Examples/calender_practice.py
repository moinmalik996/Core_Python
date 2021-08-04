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

driver.get("http://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")

driver.find_element(By.ID, "datepicker").click()

# driver.find_element(By.XPATH, "//a[text()='5']").click()

# using generic XPATH

all_dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//a")

for date_el in all_dates:
    date = date_el.text
    print(date)
    if date == "25":
        date_el.click()
        break






sleep(10)
driver.quit()

