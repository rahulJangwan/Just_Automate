from selenium import webdriver
import os
from Pages.RefactorPage import Way2


#In this test we  make changes in reactPagefile (Refactore Page) and again call same it with diffrent way.

class ClickOnEle():
    def browserOpen(self):

        #URL we are going to use
        baseUrl = "http://sims.knolskape.com/misc/react-todo/#/"

        # Chromedriver location need to be define
        DriverLocation = 'C:\Docs\Automation\Selenium\chromedriver.exe'

        # Setting enviroment veriable
        os.environ["webdriver.chrome.driver"] = DriverLocation

        # initialing Driver object  for webdriver module
        driver = webdriver.Ie(DriverLocation)
        driver.maximize_window()

        #Opening Base Url
        driver.get(baseUrl)

        driver.implicitly_wait(10)

        L1= Way2(driver)
        L1.ractToDo('Test')




Click= ClickOnEle()
Click.browserOpen()

