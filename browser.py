import undetected_chromedriver as uc
from selenium import webdriver
import json, time, ssl
from object.Params import Param
from InlineProcedure import InlineProcedure


restaurantName = "Fermi Pasta"

def getUriByKey(restaurantName) -> str:
    with open("restaurants.json") as f:
        data = json.load(f)
        for dic in data["inline"]:
            for key in dic:
                if key == restaurantName:
                    return dic[key]
    return ""

def getParameter() -> Param:
    with open("info.json") as f:
        data = json.load(f)
        if data["occasion"] == "":
            return Param(data["memberSize"], data["month&Year"], data["date"], data["time"], data["name"], data["phone"], data["email"])
        else:
            return Param(data["memberSize"], data["month&Year"], data["date"], data["time"], data["name"], data["phone"], data["email"], data["occasion"])

if __name__ == "__main__":
    ssl._create_default_https_context = ssl._create_unverified_context
    options = webdriver.ChromeOptions()
    options.headless = False
    browser = uc.Chrome(options=options)
    browser.maximize_window()
    browser.get(getUriByKey(restaurantName))

    procedure = InlineProcedure(browser, getParameter())
    procedure.selectNumbers()
    procedure.selectDateAndTime()
    procedure.keyInPersonalInformation()
    # procedure.clickBooking()
    
    time.sleep(100)


