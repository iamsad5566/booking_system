import undetected_chromedriver as uc
from selenium import webdriver
import json, time, ssl
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

if __name__ == "__main__":
    ssl._create_default_https_context = ssl._create_unverified_context
    options = webdriver.ChromeOptions()
    options.headless = False
    browser = uc.Chrome(options=options)
    # browser.maximize_window()
    browser.get(getUriByKey(restaurantName))
    procedure = InlineProcedure(browser)
    procedure.selectDateAndTime()
    
    time.sleep(200)


