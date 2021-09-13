from selenium import webdriver
from selenium.webdriver.common import options
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from time import sleep
import string

import csv
from os import path, removedirs


#///-----------------------Extract FUnction------------------------------------------///

def extract_data(file_func, field_names_func, data):
    file_exist = path.exists("data" + ".csv")
    if file_exist:
        with open(file_func, 'a', newline='', encoding='utf-8') as myfile:
            file_writer = csv.DictWriter(myfile, fieldnames=field_names_func)
            file_writer.writerow(data)
            myfile.close()
    else:
        with open(file_func, 'w', newline='', encoding='utf-8') as myfile:
            file_writer = csv.DictWriter(myfile, fieldnames=field_names_func)
            file_writer.writeheader()
            file_writer.writerow(data)
            myfile.close()

#///------------------------------END-------------------------------------------------///

#///---------------------------Column_DATA_Variables----------------------------------///

formated_date  = ""
distance       = ""
trapNo         = ""
sectionalTime  = ""
bendPosition   = ""
Position       = ""
Comment        = ""
winningTime    = ""
goingAllowance = ""
racingClass    = ""
adjustedTime   = ""

#///------------------------------END------------------------------------------------///


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()


t = 10
MyWait = Wait(driver, t)

driver.get("https://greyhoundsform.betfair.com/racingform")

meetings = MyWait.until(EC.presence_of_element_located((By.ID, "meetings")))
races    = MyWait.until(EC.presence_of_element_located((By.ID, "races")))

meetingsdd = Select(meetings)
racesdd    = Select(races)

sleep(5)

#------------------------------Locations---------------------------------

portions = ['leftColumn','rightColumn']


for index in range(1, 12):
    meetingsdd.select_by_index(index)
    options = meetingsdd.options
    op = options[index].text
    field, date = op.split(",")

    
    for index in range(1, 13):
        racesdd.select_by_index(index)
        options = racesdd.options
        race = options[index].text

        sleep(5)

        dog = 0

        for portion in portions:

            names_loc = "//*[@id='" + portion + "']/table/tbody/tr/th/h4"
            names     = MyWait.until(EC.presence_of_all_elements_located((By.XPATH, names_loc)))

            print("\n\nEntering in  :   ", portion)

            tr_index = 2
            tr_start = 2
            tr_stop  = 7
            

            for name in names:
                
                person_name = name.text
                print("Name  :  ", person_name)

                dog += 1     

                for tr_index in range(tr_start, tr_stop):
                    print("Entering in row  :  ", tr_index)

                    td_start = 1
                    td_stop  = 12

                    for td_index in range(td_start, td_stop):
                        print("Entering in column  : ", td_index)

                        formated_date_loc          = "//*[@id='" + portion +"']/table/tbody/tr["+str(tr_index)+"]/td[@class='formattedDate']"
                        distance_loc               = "//*[@id='" + portion +"']/table/tbody/tr["+str(tr_index)+"]/td[@class='distance']"
                        trapNo_loc                 = "//*[@id='" + portion +"']/table/tbody/tr["+str(tr_index)+"]/td[@class='trapNo']"
                        sectionalTime_loc          = "//*[@id='" + portion +"']/table/tbody/tr["+str(tr_index)+"]/td[@class='sectionalTime']"
                        bendPosition_loc           = "//*[@id='" + portion +"']/table/tbody/tr["+str(tr_index)+"]/td[@class='bendPosition']"
                        Position_loc               = "//*[@id='" + portion +"']/table/tbody/tr["+str(tr_index)+"]/td[@class='position']"
                        Comment_loc                = "//*[@id='" + portion +"']/table/tbody/tr["+str(tr_index)+"]/td[@class='comment']"
                        winningTime_loc            = "//*[@id='" + portion +"']/table/tbody/tr["+str(tr_index)+"]/td[@class='winningTime']"
                        goingAllowance_loc         = "//*[@id='" + portion +"']/table/tbody/tr["+str(tr_index)+"]/td[@class='goingAllowance']"
                        racingClass_loc            = "//*[@id='" + portion +"']/table/tbody/tr["+str(tr_index)+"]/td[@class='racingClass']"
                        adjustedTime_loc           = "//*[@id='" + portion +"']/table/tbody/tr["+str(tr_index)+"]/td[@class='adjustedTime']"

                        formated_date = MyWait.until(EC.presence_of_element_located((By.XPATH, formated_date_loc))).text
                        distance      = MyWait.until(EC.presence_of_element_located((By.XPATH, distance_loc))).text
                        trapNo        = MyWait.until(EC.presence_of_element_located((By.XPATH, trapNo_loc))).text
                        sectionalTime = MyWait.until(EC.presence_of_element_located((By.XPATH, sectionalTime_loc))).text
                        bendPosition  = MyWait.until(EC.presence_of_element_located((By.XPATH, bendPosition_loc))).text
                        Position      = MyWait.until(EC.presence_of_element_located((By.XPATH, Position_loc))).text
                        Comment       = MyWait.until(EC.presence_of_element_located((By.XPATH, Comment_loc))).text
                        winningTime   = MyWait.until(EC.presence_of_element_located((By.XPATH, winningTime_loc))).text
                        goingAllowance= MyWait.until(EC.presence_of_element_located((By.XPATH, goingAllowance_loc))).text
                        racingClass   = MyWait.until(EC.presence_of_element_located((By.XPATH, racingClass_loc))).text
                        adjustedTime  = MyWait.until(EC.presence_of_element_located((By.XPATH, adjustedTime_loc))).text

                    file_name     = "data" + ".csv"
                    field_names   = ['FIELD', 'DATE', 'RACE', 'DOG', 'NAME', 'F_DATE', 'DISTANCE', 'TRAP', 'BT',
                                    'BENDS', 'FINISH', 'COMMIT', 'WINNING TIME', 'G.A', 'GRADE', 'ADJUSTED TIME']
                    
                    my_dict       = {
                        'FIELD'         : field,
                        'DATE'          : date,
                        'RACE'          : race,
                        'DOG'           : dog,
                        'NAME'          : person_name,
                        'F_DATE'        : formated_date,
                        'DISTANCE'      : distance,
                        'TRAP'          : trapNo,
                        'BT'            : sectionalTime,
                        'BENDS'         : bendPosition,
                        'FINISH'        : Position,
                        'COMMIT'        : Comment,
                        'WINNING TIME'  :  winningTime,
                        'G.A'           : goingAllowance,
                        'GRADE'         : racingClass,
                        'ADJUSTED TIME' : adjustedTime
                    }

                    extract_data(file_name, field_names, my_dict)
                    print("\nData Saved")

                    


                if (tr_stop == 21):
                    break
                     

                tr_start = tr_stop + 2
                tr_stop  = tr_stop + 7


sleep(5) 





driver.quit()
