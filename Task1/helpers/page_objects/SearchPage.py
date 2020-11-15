import unicodedata

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from features.browser import Browser
from helpers.page_objects.LoginPage import LoginPage
from helpers.page_objects.EventsPage import EventsPage


class Locators():
    searchFieldXpath = "//input[@placeholder='Search ...']"
    cityFieldXpath = "//button[@id=\"dropdownMenu3\"]"
    cityDropdownXpath = "//ul[contains(@aria-labelledby, \"dropdownMenu3\")]"
    dateFromFieldName = "sf_DateFrom"
    dateToFieldName = "sf_DateTo"
    searchButtonXpath = "//button[@type = 'submit' and text() = 'Search']"
    loginButtonId = "OnlyLogin"
    firstNameFieldCLass = "first-name"
    eventLinkCssSelector = "a[href^='/EN/%s']"
    eventBuyButtonCssSelector = "button[id=btnBuy-%s]"


class SearchPage(Browser):
    def __init__(self):
        self.pageUrl = "https://www.tiketa.lt/EN/search"

    # Functions
    def goToPage(self):
        self.driver.get(self.pageUrl)

    def enterSearchField(self, caption):
        searchField = self.driver.find_element(By.XPATH, Locators.searchFieldXpath)
        searchField.send_keys(caption)
        self.driver.find_element_by_xpath("//*[@id=\"advSearchForm\"]/div[1]/div/div[1]").click()

    def selectCity(self, cityName):
        cityField = self.driver.find_element(By.XPATH, Locators.cityFieldXpath)
        cityField.click()
        cityDropDown = self.driver.find_element(By.XPATH, Locators.cityDropdownXpath)
        cities = cityDropDown.find_elements(By.TAG_NAME, "li")
        for city in cities:
            cityLink = city.find_element_by_tag_name("a")
            if cityLink.text == cityName:
                cityLink.click()

    def enterDateFrom(self, dateFrom):
        dateFromField = self.driver.find_element_by_name(Locators.dateFromFieldName)
        dateFromField.send_keys(dateFrom)

    def enterDateTo(self, dateTo):
        dateToField = self.driver.find_element_by_name(Locators.dateToFieldName)
        dateToField.send_keys(dateTo)

    def clickSearchButton(self):

        searchButton = self.driver.find_element_by_xpath(Locators.searchButtonXpath)
        searchButton.click()

    def goToLoginPage(self):
        self.driver.find_element_by_id(Locators.loginButtonId).click()
        return LoginPage(self.driver)

    def isUserLoggedIn(self):
        try:
            isUserLoggedOn = self.driver.find_element_by_class_name(Locators.firstNameFieldCLass).is_displayed()
        except:
            isUserLoggedOn = False
        return isUserLoggedOn

    def reformatEventName(self, event):
        event = unicodedata.normalize('NFD', event)
        unicodeEventName = u"".join(char for char in event if not unicodedata.combining(char))
        eventNameReformated = unicodeEventName.replace(" ", "_")
        eventNameReformated = eventNameReformated.replace("-", "")
        eventNameReformated = eventNameReformated.lower()
        return eventNameReformated

    def getEventId(self, eventLink):
        return eventLink.get_attribute("href").split("_")[-1]

    def clickBuyEventButton(self, event):
        eventLink = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                    Locators.eventLinkCssSelector % self.reformatEventName(
                                                                        event))))
        eventBuyButton = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                         Locators.eventBuyButtonCssSelector % self.getEventId(
                                                                             eventLink))))
        eventBuyButton.click()
        return EventsPage(self.driver)
