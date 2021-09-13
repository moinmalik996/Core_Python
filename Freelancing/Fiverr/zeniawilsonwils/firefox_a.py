from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager import firefox
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import subprocess


# profile_path = input("Enter the Firefox Profile Path : ")
# profile = webdriver.FirefoxProfile(profile_path)

opt = Options()
opt.headless = True

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=opt)
session_id = driver.session_id
print()


print("Session ID  :  ", session_id)

#-----------------------------------------------------------------------------------------------------


subprocess.call("start https://iwastesomuchtime.com/random", shell=True)


