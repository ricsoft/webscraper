from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re

def getChromeDriver():
    chromeOptions = Options()
    chromeOptions.add_argument('--no-sandbox')
    chromeOptions.add_argument('--headless')
    chromeOptions.add_argument('--disable-gpu')

    return webdriver.Chrome(options=chromeOptions)

def fillBeerList(driver, url, waitFor, beerName, beerType=None):
    beerList = []
    beerNames = []

    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, waitFor)))

    for name in beerName:
        beerNames = beerNames + driver.find_elements_by_css_selector(name)

    if beerType:
        beerTypes = driver.find_elements_by_css_selector(beerType)

    for i in range(len(beerNames)):
        if beerType:
            beer = {
                'name': beerNames[i].get_attribute('textContent'),
                'type': beerTypes[i].get_attribute('textContent')
            }
        else:
            beer = {
                'name': beerNames[i].get_attribute('textContent')
            }

        beerList.append(beer)
    
    return beerList

def stripNewLine(beerList):
    for obj in beerList:
        obj['name'] = obj['name'].rstrip("\n")

    return beerList

def spaceBeforeCapital(beerList):
    for obj in beerList:
        obj['name'] = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', obj['name'])

    return beerList