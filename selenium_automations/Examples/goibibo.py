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

driver.get("https://www.goibibo.com/")

departure_celender = driver.find_element(By.XPATH, "//input[@id='departureCalendar']").click()
select_date        = driver.find_element(By.XPATH, "//div[text()='25']").click()

sleep(3)

return_calender   = driver.find_element(By.XPATH, "//input[@id='returnCalendar']").click()
select_date       = driver.find_elements(By.XPATH, "//div[@class='calDate']")

for date_el in select_date:
    date = date_el.text
    print(date)
    if date == "26":
        date_el.click()
        break



sleep(10)
driver.quit()

