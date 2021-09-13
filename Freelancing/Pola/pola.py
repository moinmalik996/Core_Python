from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import subprocess

t = 10

driver = webdriver.Chrome(executable_path= ChromeDriverManager().install())

driver.get("https://www.youtube.com/playlist?list=PL6Bh4E9jHyGD3E23-FH2R72SN_kY5hhe-")


sleep(10)

playlistloc = "//a[@class='yt-simple-endpoint style-scope ytd-playlist-video-renderer']"

playlistlinks = Wait(driver, t).until(EC.presence_of_all_elements_located((By.XPATH, playlistloc)))

for link in playlistlinks:
    linkurl = link.get_attribute("href")
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(linkurl)

    dot_menu_loc = "/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/yt-icon-button/button/yt-icon"
    dor_nemu = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, dot_menu_loc))).click()

    sleep(2)
    
    open_trans_loc = "//tp-yt-paper-listbox[@id='items']/ytd-menu-service-item-renderer[2]"
    open_trans = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, open_trans_loc))).click()

    sleep(2)

    driver.close()
    driver.switch_to.window(driver.window_handles[0])


driver.quit()