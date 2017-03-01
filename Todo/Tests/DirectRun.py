from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By


#Direct run is created to show how we can write test senarios wothout any framework.
#in this we make use of Customized Wait type which is part of Utility package


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

        TextIdLocator=driver.find_element(By.XPATH, "//input[@class='new-todo']")
        TextIdLocator.send_keys('test')
        TextIdLocator.submit()
        click1=driver.find_elements(By.XPATH,"//input[@class='toggle']")

        size = len(click1)
        print("Size of the click1: " + str(size))

        for radioButton in click1:
            isSelected = radioButton.is_selected()

            if not isSelected:
                radioButton.click()
                time.sleep(2)


        #Checking for hidden element clear complete
        HiddenElement = driver.find_element_by_css_selector('.clear-completed')
        print("Element visible? " + str(HiddenElement.is_displayed()))
        HiddenElement.click()


        #Case2 Clicking on ALL section.
        TextIdLocator = driver.find_element(By.XPATH, "//input[@class='new-todo']")
        TextIdLocator.send_keys('test')
        TextIdLocator.submit()
        click1 = driver.find_elements(By.XPATH, "//input[@class='toggle']")
        ALL=driver.find_element_by_css_selector('.selected')
        ALL.click()

        #Case3 clicking on completed
        TextIdLocator = driver.find_element(By.XPATH, "//input[@class='new-todo']")
        TextIdLocator.send_keys('test')
        TextIdLocator.submit()
        click1 = driver.find_elements(By.XPATH, "//input[@class='toggle']")
        Completed = driver.find_element_by_css_selector('.filters > li > a')
        Completed.click()


Click= ClickOnEle()
Click.browserOpen()
