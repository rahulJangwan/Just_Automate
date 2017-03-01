from selenium.webdriver.common.by import By
import time

class Page1():

    def __init__(self, driver):
        self.driver = driver

    def ractToDo(self,Type):


        TextIdLocator = self.driver.find_element(By.XPATH, "//input[@class='new-todo']")
        TextIdLocator.send_keys(Type)
        TextIdLocator.submit()
        click1 = self.driver.find_elements(By.XPATH, "//input[@class='toggle']")

        size = len(click1)
        print("Size of the click1: " + str(size))

        for radioButton in click1:
            isSelected = radioButton.is_selected()

            if not isSelected:
                radioButton.click()
                time.sleep(2)

        # Checking for hidden element clear complete
        HiddenElement = self.driver.find_element_by_css_selector('.clear-completed')
        print("Element visible? " + str(HiddenElement.is_displayed()))
        HiddenElement.click()

        # Case2 Clicking on ALL section.
        TextIdLocator = self.driver.find_element(By.XPATH, "//input[@class='new-todo']")
        TextIdLocator.send_keys(Type)
        TextIdLocator.submit()
        click1 = self.driver.find_elements(By.XPATH, "//input[@class='toggle']")
        ALL = self.driver.find_element_by_css_selector('.selected')
        ALL.click()

        # Case3 clicking on completed
        click1 = self.driver.find_elements(By.XPATH, "//input[@class='toggle']")
        Completed = self.driver.find_element_by_css_selector('.filters > li > a')
        Completed.click()