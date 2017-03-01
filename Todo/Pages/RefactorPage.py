
#We refectore reactPagefile in this programm.

from selenium.webdriver.common.by import By
import time


class Way2():
    def __init__(self, driver):
        self.driver = driver


    #LOCATORS
    text_box_locator= "//input[@class='new-todo']"
    checkBox_="//input[@class='toggle']"
    HiddenElemt_=".clear-completed"
    All_Locator_='.selected'
    CompleteLink='.filters > li > a'

    def textBoxLocator(self):
        return self.driver.find_element(By.XPATH,self.text_box_locator )

    def enterText(self, Type):
        a=self.textBoxLocator().send_keys(Type)
        a.subbmit()


    def clickRadioButton(self):
        click1 =self.driver.find_elements(By.XPATH,self.checkBox_)
        size = len(click1)
        print("Size of the click1: " + str(size))

        for radioButton in click1:
            isSelected = radioButton.is_selected()

            if not isSelected:
                radioButton.click()
                time.sleep(2)

    #Checking for hidden element clear complete
    def HiddenElemment(self):
        HiddenElement = self.driver.find_element_by_css_selector(self.HiddenElemt_)
        print("Element visible? " + str(HiddenElement.is_displayed()))
        HiddenElement.click()


    def clickAllLink(self):
        TextIdLocator = self.driver.find_element(By.XPATH,self.text_box_locator )
        TextIdLocator.send_keys(Type)
        TextIdLocator.submit()
        click1 = self.driver.find_elements(By.XPATH, self.checkBox_)
        size = len(click1)
        print("Size of the click1: " + str(size))

        for radioButton in click1:
            isSelected = radioButton.is_selected()

            if not isSelected:
                radioButton.click()
                time.sleep(2)

        ALL = self.driver.find_element_by_css_selector(self.All_Locator_)
        ALL.click()

    def completeClick(self):
        Completed = self.driver.find_element_by_css_selector(self.CompleteLink)
        Completed.click()


    def ractToDo(self,Type):
        m=self.textBoxLocator()
        m.click()
        self.enterText("FINDOUT")
        self.clickRadioButton()
        #Checking hidden element is Displayed
        self.HiddenElemment()

        #After clicking hidden element case will close so retype same thing and check
        self.clickAllLink()
        self.completeClick()


