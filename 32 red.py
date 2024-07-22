from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait #(html slower)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time

    ##OPTIONS#
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

    ##DRIVER
driver_path="F:\chromedriver.exe"


try:

##WEB 32RED
    driver=webdriver.Chrome(executable_path=driver_path,chrome_options=options)
    driver.get("https://www.32red.com/casino/progressive-jackpot-games")

    time.sleep(10)


  ##########CLOSE COOKIES######    

    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Allow all ')]")))\
    .click()
    time.sleep(3) 

except Exception as e:
    
        print(f"An error occurred: {e}")
        print("This route has changed.It should be reviewed")
        driver.quit()  ###Closing Web ####
 
 
 
####Browsing the entire website####
 
try:       

    driver.execute_script("window.scrollBy(0, 100);")  # Scroll down
    time.sleep(5)

    max_attempts=10
    attempt = 0

    while attempt < max_attempts:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
        '//*[@id="2041"]//div[contains(@class,"pagin")]/a[contains(@class,"arrow next")]/i[@class="icon-arrow-right"]'                                                                                                                            
        '')))\
        .click()
        time.sleep(3)
    
        attempt += 1
    
    time.sleep(5)

    driver.execute_script("window.scrollBy(0, 600);")  # Scroll down
    time.sleep(5)


    max_at=5
    att = 0
    while att < max_at:
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH,
        '//*[@id="2043"]//div[contains(@class,"pagin")]/a[contains(@class,"arrow next")]/i[@class="icon-arrow-right"]'                                                                                                                            
        '')))\
        .click()
    
        att += 1
        time.sleep(3)
    
    driver.execute_script("window.scrollBy(0, 600);")  # # Scroll down
    time.sleep(2)


    max_at=5
    att = 0
    while att < max_at:
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH,
        '//*[@id="2045"]//div[contains(@class,"pagin")]/a[contains(@class,"arrow next")]/i[@class="icon-arrow-right"]'                                                                                                                            
        '')))\
        .click()
    
        att += 1
        time.sleep(5)
        
    time.sleep(10)
    
    
except Exception as e:
    
        print(f"An error occurred: {e}")
        print("the website was not browsed correctly.It should be reviewed")
        driver.quit()  ###Closing Web ####


#######VALUES AND NAMES ON THIS 32RED##

###This is the same xpath for Both

elements_xpath=  '//*[@id="2041"]//div//div[img[@alt] and //span/span[contains(@class,"jackpot-value")]/span] '


try:
    
#####VALUES#####

    elements_value_data = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, elements_xpath)))
      
    values_data = []

    for element in elements_value_data:
        value = element.text
        values_data.append(value)
           
    #x=(len(values_data))

    #print(values_data)
       
       
   ####Data fixed       
       
    import re
    def process_value_data(span_text):
        if not span_text.strip():
            return "No value"  ###I did not get value without logging in
        match = re.search(r'£([\d,]+(?:\.\d+)?)', span_text)
        return match.group(1).replace(',', '') if match else span_text

###Processing all values
    processed_values = [process_value_data(value) for value in values_data]
    print("Valores del atributo 'alt':", processed_values)

        
#########NAMES#####

    elements_name_data = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, elements_xpath)))

    names_data = []

    for element_data in elements_name_data:
        img_element = element_data.find_element_by_xpath(".//img[@alt]")
        alt_value = img_element.get_attribute("alt")
        names_data.append(alt_value)
    
    #y=(len(names_data))

    #print(names_data)

    #print(f"number of names are {y}")
    #print(f"number of values are {x}")
    
except Exception as e:
    
    print(f"An error occurred: {e}")
    print("There has a mistake with the route.It should be reviewed")


#######DATA FRAMES######

try:
    import pandas as pd
     
    ####Data Frame with all games
    
    df = pd.DataFrame({"Name": names_data, "Pool_Value": processed_values })
    
    print(df) ###All games

    ###Data Frame with jackpots only
    
    ##Change to numeric Pool Value, no-numeric to NaN 
    df["Pool_Value"] = pd.to_numeric(df["Pool_Value"], errors='coerce')

    #Filter no-numeric values
    df_filtered = df.dropna(subset=["Pool_Value"])

    print(df_filtered)

except Exception as e:
    
    print(f"An error occurred: {e}")
    print("There has a mistake. Pandas, Names, or Pools should be reviewed")
    

driver.quit()  ###Closing Web ####