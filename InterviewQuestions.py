from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.events import AbstractEventListener,EventFiringWebDriver
from selenium.webdriver.common.by import By
import os
from selenium.common.exceptions import NoSuchElementException


class MyCustomListener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print(f"Navigating to url: {url}")
        return super().before_navigate_to(url, driver)
    def before_find(self, by, value, driver):
        print(f"found the value: {value}")
        return super().before_find(by, value, driver)
    

def findElementByText(driver,txt,tag):
    elements = driver.find_elements(By.TAG_NAME,tag)
    for element in elements:
        if txt in element.text:
            return element
        else:
            raise NoSuchElementException(f"{element} is not there")

driverDir = os.makedirs(os.getcwd() + "//drivers",exist_ok=True)
service = Service(os.getcwd() + "//drivers//msedgedriver.exe")
options = webdriver.EdgeOptions()
options.add_argument("--disable-gpu")
options.add_argument("--start-maximized")
smallTimeout = 10
largeTimeout = 30
driver = webdriver.Edge(service=service,options=options)
listenerDriver = EventFiringWebDriver(driver,MyCustomListener())

listenerDriver.get("https://www.redbus.in/")
WebDriverWait(listenerDriver,smallTimeout).until(EC.presence_of_element_located((By.CSS_SELECTOR,"[title='redBus']")))
# element = findElementByText(listenerDriver,"From","div")
# element.click()
# # element.send_keys("Kolkata")
# import time
# time.sleep(10)


import requests
url = 'https://jsonplaceholder.typicode.com/todos/1'
response = requests.get(url)

print(response.json())

payload = {
    "name": "Alex",
    "Age": 23
}

response = requests.post(url,payload)
print(response.status_code)


   