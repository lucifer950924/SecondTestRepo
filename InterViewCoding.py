def countRepeatingChars(sampleString = ""):
    
    uniqueStringList = list(set(list(sampleString.__iter__())))
    samplestringcount = [{i:sampleString.count(i)} for i in uniqueStringList]
    print(samplestringcount)
    


countRepeatingChars("Balloon")


def filtEvenNumbers(sampleNumber = 12345):
    print([i for i in list(str(sampleNumber).__iter__()) if int(i)%2 == 0])

filtEvenNumbers(22243678)


from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import os


options = webdriver.EdgeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
os.makedirs(os.getcwd() + "//drivers",exist_ok=True)
print(os.getcwd() + "//drivers")
service = Service(os.getcwd() + "//drivers//msedgedriver.exe")


driver = webdriver.Edge(service=service,options=options)


driver.get("https://www.google.com")
driver.maximize_window()

# WebDriverWait(driver=driver,timeout=10).until(EC.text_to_be_present_in_element("Google"))
WebDriverWait(driver=driver,timeout=10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"[title='Search']"))).send_keys("Pokemon")
WebDriverWait(driver=driver,timeout=10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"[title='Search']"))).send_keys(Keys.ENTER)
# WebDriverWait(driver=driver,timeout=10).until(EC.text_to_be_present_in_element("Google"))
time.sleep(2)













