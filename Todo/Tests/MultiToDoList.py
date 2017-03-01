from selenium import webdriver
from pages.GenricToDoMethods import Way2
import unittest
import pytest
from ddt import ddt, data, unpack

#Inheriting Unitest class
class ClickOnEle(unittest.TestCase):


        #URL we are going to use
        baseUrl = "http://sims.knolskape.com/misc/react-todo/#/"

        # Chromedriver location need to be define
        DriverLocation = 'C:\Docs\Automation\Selenium\chromedriver.exe'

        # Setting enviroment veriable
        os.environ["webdriver.chrome.driver"] = DriverLocation

        # initialing Driver object  for webdriver module
        driver = webdriver.Ie(DriverLocation)
        driver.maximize_window()

        M=Way2(driver)

        @pytest.mark.run(order=1)
        def CheckingFunction(self):
            self.driver.get(self.baseUrl)
            self.M.ractToDo("Gym_Time")

        #Multiple task enter with help of CSV

        @pytest.mark.run(order=1)
        @data(("Take Food"), ("Sleep"))
        @unpack
        def MultipleInput(self, Type):
            self.driver.get(self.baseUrl)
            self.M.ractToDo(Type)

