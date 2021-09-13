import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException


opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:5005")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

session_id   = driver.session_id

# driver.get("https://google.com")

# driver.get("https://facebook.com")

driver.get("https://youtube.com")

print(session_id)

