from robot.api import logger
from selenium.webdriver.support.events import AbstractEventListener
from robot.running.model import TestSuite
import pandas as pd
from robot.running.model import UserKeyword
class   Listener1(AbstractEventListener):
    ROBOT_LISTENER_API_VERSION = 3
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    def __init__(self):
        self.te = [] 
        self.res = []
        self.su = []
        self.current_suite = None
        
    def start_suite(self, suite,driver):
        self.current_suite = suite
        self.su.append(suite)
        logger.console(f'The suite:{suite} is starting')
        
        #tc.keywords.create(name=kwname, args=args) #deprecated in 4.0
        
        
        # for test in suite.tests:
        #     if test !='MyTC1':
        #         if test.tags == 'TC2':
        #             tc = self.current_suite.tests.create(name='MyTC1')
        #             # tc.body.create_keyword(name='ukw')
        #             tc.body = test.body 
        tc = self.current_suite.tests.create(name='MyTC2')
        tc.body = suite.resource.keywords(name = 'Another TC').body
                
        
        
    def end_test(self,test,result):
        logger.console(f'The test {test} has ended')
        logger.console(result.status)
        self.te.append(test)    
        self.res.append(result.status)    
            
        
        
        data= {'test_suite':pd.Series(self.su),'test_case_name':pd.Series(self.te),'result':pd.Series(self.res)}
        
        df = pd.DataFrame(data)
        writer = pd.ExcelWriter('C:/Users/death/Documents/Python_IDEA/Automation/Python_Files/df.xlsx')
        df.to_excel(writer)
        writer.save()
import unittest
class test_TC01(unittest.TestCase):
    def test_TC01():
        from selenium import webdriver
        webdriver.Chrome().get('https://www.demoblaze.com/')


        

