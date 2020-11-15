from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from features.browser import Browser


class Locators():
    tiketaLogoClassName = "tiketa-logo"
    sectorsDivCssSelector = "g[class='main']"
    sectorButtonsCssSelector = "g[class='sector']"
    sectorIframeId = "frame"


class SectorsPage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def clickSectorButton(self, sectorName):
        tiketaLogo = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "tiketa-logo")))
        tiketaLogo.send_keys(Keys.PAGE_DOWN)
        self.driver.switch_to.frame('frame')
        self.driver.implicitly_wait(1)
        sectorsDiv = self.driver
        sectorsDiv = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "g[class='main']")))
        sectorButtons = sectorsDiv.find_elements_by_css_selector("g[class='sector']")
        for sectorButton in sectorButtons:
            if sectorButton.text == sectorName:
                sectorButton.click()
                break
