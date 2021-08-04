from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from time import sleep
import openpyxl




product_name = "Buchstabenperlen"
wb = openpyxl.load_workbook("Selenium_Automations/EC DATA UPLOADING/Buchstabenperlen/" + product_name + ".xlsx")
kw_sheet = wb['Keywords']


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
t = 5


driver.get("https://login.ec.com.pk/login?redirect=https%3A%2F%2Fdashboard.ec.com.pk")

login_loc = "//input[@id='email']"
pass_loc  = "//input[@id='password']"
login_btn_loc = "//button[@type='submit']"

login = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, login_loc)))
login.send_keys("moin.malik996@gmail.com")


passW = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, pass_loc)))
passW.send_keys("m@l!kec1234")

login_btn = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, login_btn_loc)))
login_btn.click() 

sleep(2)

driver.get("https://dashboard.ec.com.pk/products")

product_link_loc = "//a[text()='" + product_name + "']"
product_link = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, product_link_loc)))
product_link.click()



"""
Inputs Locations
"""
keyword_loc        = "//input[@name='keyword']"
MW_loc             = "//input[@name='merchant_words_search_volume']"
JS_Sales_loc       = "//input[@name='js_average_monthly_sales']"
h10_sv_loc         = "//input[@name='h10_search_volume']"
cpr_GAs_loc        = "//input[@name='cpr_8_day_giveaways']"
competing_prod_loc = "//input[@name='competing_products']"
js_score_loc       = "//input[@name='js_score']"
vl_score_loc       = "//input[@name='vl_score']"

"""
Select Locations
"""

sale_rev_loc       = "//select[@name='sales_revenue_depth_id']"
reviews_loc        = "//select[@name='reviews']"
review_rat_loc     = "//select[@name='review_rating']"
amazon_dom_loc     = "//select[@name='amazon_dominance']"
brand_dom_loc      = "//select[@name='brand_dominance']"
price_depth_loc    = "//select[@name='price_depth_id']"


"""
File Locations
"""
js_file_loc        = "//input[@name='js_screenshot']"
h10_file_loc       = "//input[@name='h10_keyword_graph']"
top10_file_loc     = "//input[@name='amazon_search_screenshot']"
seasnlty_file_loc  = "//input[@name='seasonality_graph']"

row_records = "EFGHIJKLMN"

for loop in range(1, 11):
    for row in range(0, len(row_records)):
        
        sleep(3)
        # Inputs

        keyword         = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, keyword_loc)))
        MW              = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, MW_loc)))
        JS_sales        = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, JS_Sales_loc)))
        h10_sv          = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, h10_sv_loc)))
        cpr_GAs         = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, cpr_GAs)))
        competing_prod  = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, competing_prod_loc)))
        js_score        = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, js_score_loc)))
        vl_score        = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, vl_score_loc)))

        # Selects

        sale_rev     = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, sale_rev_loc)))
        reviews      = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, reviews_loc)))
        review_rat   = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, review_rat_loc)))
        amazon_dom   = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, amazon_dom_loc)))
        brand_dom    = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, brand_dom_loc)))
        price_depth  = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, price_depth_loc)))

        # Assigning Selects

        sale_rev_dd      = Select(sale_rev)
        reviews_dd       = Select(reviews)
        review_rat_dd    = Select(review_rat)
        amazon_dom_dd    = Select(amazon_dom) 
        brand_dom_dd     = Select(brand_dom)
        price_depth_dd   = Select(price_depth)

        # Files

        js_file     = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, js_file_loc)))
        h10_file    = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, h10_file_loc)))
        top10_file  = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, top10_file_loc)))
        seasonality = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, seasnlty_file_loc)))


        # Giving Inputs

        keyword.send_keys(kw_sheet[row_records[row]+str(2)])
        MW.send_keys(kw_sheet[row_records[row]+str(3)])
        JS_sales.send_keys(kw_sheet[row_records[row]+str(4)])
        h10_sv.send_keys(kw_sheet[row_records[row]+str(11)])
        cpr_GAs.send_keys(kw_sheet[row_records[row]+str(12)])
        competing_prod.send_keys(kw_sheet[row_records[row]+str(13)])
        js_score.send_keys(kw_sheet[row_records[row]+str(14)])
        vl_score.send_keys(kw_sheet[row_records[row]+str(15)])

        # Giving Selects

        sale_rev_dd.select_by_visible_text(kw_sheet[row_records[row]+str(5)])
        reviews_dd.select_by_visible_text(kw_sheet[row_records[row]+str(6)])
        review_rat_dd.select_by_visible_text(kw_sheet[row_records[row]+str(7)])
        amazon_dom_dd.select_by_visible_text(kw_sheet[row_records[row]+str(8)])
        brand_dom_dd.select_by_visible_text(kw_sheet[row_records[row]+str(9)])
        price_depth_dd.select_by_visible_text(kw_sheet[row_records[row]+str(10)])

        # Giving Files

        js_file.send_keys("\\Selenium_Automations\\EC DATA UPLOADING\\Buchstabenperlen\\"+ str(loop) + "\\js.PNG")
        h10_file.send_keys("\\Selenium_Automations\\EC DATA UPLOADING\\Buchstabenperlen\\"+ str(loop) + "\\h10.PNG")
        top10_file.send_keys("\\Selenium_Automations\\EC DATA UPLOADING\\Buchstabenperlen\\"+ str(loop) + "\\top10.PNG")
        seasonality.send_keys("\\Selenium_Automations\\EC DATA UPLOADING\\Buchstabenperlen\\"+ str(loop) + "\\seasonality.PNG")


        submit_btn_loc = "//button[@type='submit']"
        submit = Wait(driver, t).until(EC.presence_of_element_located((By.XPATH, submit_btn_loc))).click()



driver.quit()