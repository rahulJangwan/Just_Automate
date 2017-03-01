from selenium import webdriver
import os
from Pages.reactPagefile import Page1

from selenium.webdriver.common.by import By

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

        driver.implicitly_wait(50)

        L1= Page1(driver)
        L1.ractToDo('Test')




Click= ClickOnEle()
Click.browserOpen()

