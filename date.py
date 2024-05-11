from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from datetime import datetime as dt
from dateutil import parser
# //td[@class="dt-right dt-body-right"]
driver = webdriver.Chrome()
driver.get('https://datatables.net/')
driver.maximize_window()
wait(driver,5).until(EC.presence_of_element_located((by.XPATH,'//h1[contains(@data-anchor,"Add-advanced-interaction-controls")]')))
# time.sleep(1)
# element = lambda x : '(//td[@class="dt-right dt-body-right"])' + [x]
# for i in range(11):
    
wait(driver,5).until(EC.presence_of_element_located((by.XPATH,'//td[@class="dt-right dt-body-right"]')))
date = driver.find_element(by.XPATH,'//td[@class="dt-right dt-body-right"]').text
print(date)
date_obj = parser.parse(date).strftime("%d-%m-%Y")
# dat = dt.strptime(date,"%d-%m-%y")
print(date_obj)
# This is for second push