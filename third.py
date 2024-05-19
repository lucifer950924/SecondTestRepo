from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from robot.api.deco import keyword
from selenium.webdriver.common.keys  import Keys 
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

@keyword

def fetch_text_from_wiki(serach_term="Indian cormorant"):
    driver = webdriver.Chrome()
    driver.get('https://www.google.com')
    driver.maximize_window()
    wait(driver,10).until(EC.presence_of_element_located((by.XPATH,"//*[contains(text(),'Google')]//following::textarea")))
    element= driver.find_element(by.XPATH,"//*[contains(text(),'Google')]//following::textarea")
    element.send_keys(serach_term)
    element.send_keys(Keys.ENTER)
    wait(driver,10).until(EC.presence_of_element_located((by.XPATH,"//*[contains(text(),'Wikipedia')]")))
    driver.find_element(by.XPATH,"//*[contains(text(),'Wikipedia')]").click()
    list_of_sections = ['Taxonomy','Description','Distribution and habitat','Behaviour']
    # list_of_elements = list(map(lambda x: "//span[contains(text(),'" + x + "')]",list_of_sections))
    f = lambda x: "//span[contains(text(),'" + x + "')]"
    wait(driver,10).until(EC.presence_of_element_located((by.XPATH,f(serach_term))))
    list_of_elements_text = list(map(lambda x: '//span[contains(text(),"' + x +'")]//following::p',list_of_sections))
    print(list_of_elements_text)
    # list(map(lambda x: driver.execute_script("arguments[0].scrollIntoView();", x),list_of_elements_text))
    map(lambda x: ActionChains(driver).move_to_element(x).perform(),list_of_elements_text)
    list_of_texts = list(map(lambda x: driver.find_element(by.XPATH,x).text,list_of_elements_text))
    print(list_of_texts)
    df = pd.DataFrame({'section':list_of_sections,'texts':list_of_texts})
    df.to_excel('output.xlsx')
    return  list_of_texts


    

