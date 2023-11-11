from BookingProcedure import BookingProcedure
from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Type
from object.Params import Param
from module.Iterator import Iterator
import time

class InlineProcedure(BookingProcedure):
    def __init__(self, driver: Type[Chrome], parameter: Type[Param]):
        self.browser = driver
        self.param = parameter
        self.itr = Iterator(driver, parameter)

    def selectNumbers(self):
        peopleButton: Type[WebElement] = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID,"adult-picker")))
        self.browser.execute_script("window.scrollTo(" + str(peopleButton.location['x']) + "," + str(peopleButton.location['y']-100)+")")
        time.sleep(1)
        peopleButton.click()
        peopleStr = "#adult-picker > option:nth-child({people})"
        self.itr.itrNumber(peopleStr)

    def selectDateAndTime(self):
        dateButton: Type[WebElement] = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID,"date-picker")))
        self.browser.execute_script("window.scrollTo(" + str(dateButton.location['x']) + "," + str(dateButton.location['y'])+")")
        time.sleep(2)
        dateButton.click()
        dates = "#calendar-picker > div.sc-gsnTZi.{section} > div.sc-papXJ.dxZnaq > div:nth-child({row}) > div:nth-child({column})"
        targetSection = "hzknaT"
        if self.browser.find_element(by=By.CSS_SELECTOR, value="#calendar-picker > div.sc-gsnTZi.flPLDk > div.sc-gsnTZi.kMDMoU > h4").text == self.param.getMonth():
            targetSection = "flPLDk"
        
        prevState: str = self.browser.find_element(by=By.CSS_SELECTOR, value="#book-now-action-bar > div.sc-kgUAyh.gIlZKk > div.sc-gsnTZi.hzPtvw > button").text
        targetDate: Type[WebElement] = self.itr.itrTheDate(selector=dates, targetSection=targetSection)
        try:
            targetDate.click()
        except:
            return
        currState: str = self.browser.find_element(by=By.CSS_SELECTOR, value="#book-now-action-bar > div.sc-kgUAyh.gIlZKk > div.sc-gsnTZi.hzPtvw > button").text
        if currState == prevState:
            return
        
        timePath = "//*[@id=\"book-now-content\"]/div[2]/button[{seq}]"
        self.itr.itrTheTime(timePath)
        try:
            self.browser.find_element(by=By.CSS_SELECTOR, value="#book-now-action-bar > div.sc-gsnTZi.hMpglF > button > div").click()
        except:
            return
        
        try:
            time.sleep(1)
            confirm: Type[WebElement] = self.browser.find_element(by=By.XPATH, value="/html/body/div[5]/div/div/div/div[3]/button")
            confirm.click()
        except:
            return
        
        print("sucess")
        
             
    def keyInPersonalInformation(self):
        self.browser.execute_script("window.scrollTo(0,0)")
        time.sleep(1)
        nameInput: Type[WebElement] = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID,"name")))
        nameInput.send_keys(self.param.getName())

        phoneInput: Type[WebElement] = self.browser.find_element(by=By.CSS_SELECTOR, value="#phone")
        phoneInput.send_keys(self.param.getPhone())

        emailInput: Type[WebElement] = self.browser.find_element(by=By.CSS_SELECTOR, value="#email")
        emailInput.send_keys(self.param.geteMail())

        occasions = "#contact-form > section > div.sc-gsnTZi.kdHcWt > div.sc-gsnTZi.dWSQQD > div:nth-child({occasion})"
        self.itr.itrTheOccasions(occasions)

    def creditCardInformation(self):
        return "ddd"
    def clickBooking(self):
        booking: Type[WebElement] = self.browser.find_element(by=By.CSS_SELECTOR, value="#contact-form > div > button.sc-hHLeRK.jmEJIc > div")
        self.browser.execute_script("window.scrollTo(" + str(booking.location['x']) + "," + str(booking.location['y']-100)+")")
        time.sleep(1)
        booking.click()
    

