from BookingProcedure import BookingProcedure
from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Type
import time

class InlineProcedure(BookingProcedure):
    def __init__(self, driver: Type[Chrome]):
        self.browser = driver
    def selectDateAndTime(self, memberSize=2, date="November 11", timePoint="17:30"):
        dateButton: Type[WebElement] = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID,"date-picker")))
        self.browser.execute_script("window.scrollTo(" + str(dateButton.location['x']) + "," + str(dateButton.location['y'])+")")
        time.sleep(2)
        dateButton.click()
        dates = "#calendar-picker > div.sc-gsnTZi.hzknaT > div.sc-papXJ.dxZnaq > div:nth-child({row}) > div:nth-child({column})"
        
        for i in range(1, 6):
            for j in range(1, 8):
                try:
                    curr: Type[WebElement] = self.browser.find_element(by=By.CSS_SELECTOR, value=dates.format(row=i, column=j))
                    #calendar-picker > div.sc-gsnTZi.hzknaT > div.sc-gsnTZi.kMDMoU > h4
                    #calendar-picker > div.sc-gsnTZi.hzknaT > div.sc-gsnTZi.kMDMoU > h4
                    content: str = curr.get_dom_attribute("data-date")
                    print(content)
                except:
                    pass
             
    def keyInPersonalInformation(self):
        return "ccc"
    def creditCardInformation(self):
        return "ddd"
    def clickBooking(self):
        return "kkk"
    

