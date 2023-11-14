from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import Type
from object.Params import Param
import time

class Iterator:
    def __init__(self, driver: Type[Chrome], parameter: Type[Param]):
        self.browser = driver
        self.param = parameter

    def itrNumber(self, selector: str):
        number: Type[WebElement] = self.browser.find_element(by=By.CSS_SELECTOR, value=selector.format(people=str(self.param.getMemberSize())))
        number.click()

    def itrTheDate(self, selector: str, targetSection: str) -> Type[WebElement]:
        for i in range(1, 6):
            for j in range(1, 8):
                try:
                    curr: Type[WebElement] = self.browser.find_element(by=By.CSS_SELECTOR, value=selector.format(section=targetSection, row=i, column=j))
                    content: str = curr.text.split("\n")[0]
                    if(content == self.param.getDate()):
                        return curr
                except:
                    pass
        return WebElement
    
    def itrTheTime(self, xPath: str):
        for i in range(1, 5):
            dTime: Type[WebElement] = self.browser.find_element(by=By.XPATH, value=xPath.format(seq=i))
            if i == 1:
                self.browser.execute_script("window.scrollTo(" + str(dTime.location['x']) + "," + str(dTime.location['y']-100)+")")
                time.sleep(1)
            if dTime.text == self.param.getTime():
                dTime.click()
                return
            
    def itrTheOccasions(self, selector: str):
        for i in range(1, 7):
            box: Type[WebElement] = self.browser.find_element(by=By.CSS_SELECTOR, value = selector.format(occasion=i))
            if i == 1:
                self.browser.execute_script("window.scrollTo(" + str(box.location['x']) + "," + str(box.location['y'])+")")
                time.sleep(1)

            if box.text == self.param.getOccasion():
                box.click()
                return