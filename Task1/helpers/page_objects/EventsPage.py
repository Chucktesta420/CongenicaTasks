from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from features.browser import Browser
from helpers.page_objects.SectorsPage import SectorsPage


class Locators():
    eventDivsCssSelector = "div[class='page-content col-xs-12']"
    eventNameHeader = "//h4[contains(text(), '%s ')]"
    eventPriceSpan = "//span[contains(text(), '%s')]"
    eventBuyButtonLinkCssSelector = "a[href*='Purchase']"


class EventsPage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def clickBuyEventTicketButton(self, eventName, eventPrice):
        eventElementList = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, Locators.eventDivsCssSelector)))
        for eventElement in eventElementList:
            try:
                eventName = eventElement.find_element_by_xpath(Locators.eventNameHeader % eventName)
                eventPrice = eventElement.find_element_by_xpath(Locators.eventPriceSpan % eventPrice)
            except:
                eventName = None
                eventPrice = None
            if eventName != None and eventPrice != None:
                eventBuyButton = eventElement.find_element_by_css_selector(Locators.eventBuyButtonLinkCssSelector)
                eventBuyButton.click()
                break
        return SectorsPage(self.driver)