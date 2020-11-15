import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# WebDriver setup
currentDir = os.getcwd()
chromedriverPath = os.path.join(currentDir, ".\\chromedriver.exe")
driver = webdriver.Chrome(executable_path=chromedriverPath)
driver.get("http://the-internet.herokuapp.com/challenging_dom")
driver.maximize_window()

# Getting table elements
tableHeaders = driver.find_elements_by_tag_name("th")
tableRows = driver.find_elements_by_tag_name("tr")
elementsToHighlight = []  # array to store elements that need to be highlighted


def highlightElement(element):
    actions = ActionChains(driver)
    if element.tag_name == 'a':
        xoffsetFrom = -1
        yoffsetFrom = 0
        xoffsetTo = element.size['width']
        yoffsetTo = element.size['height']
        actions.move_to_element_with_offset(element, xoffsetFrom, yoffsetFrom) \
            .click_and_hold(on_element=None) \
            .release().click_and_hold(on_element=None) \
            .move_to_element_with_offset(element, xoffsetTo, yoffsetTo) \
            .release().perform()
        actions.reset_actions()
    else:
        actions.double_click(on_element=element).perform()


def getTextElementOfRowInColumn(columnName, rowNumber):
    for headerIndex in range(len(tableHeaders)):
        if tableHeaders[headerIndex].text == columnName:
            rowToHighlight = getTdElement(headerIndex, tableRows[rowNumber])
            return rowToHighlight


def getTdElement(columnIndex, tableRow):
    return tableRow.find_elements_by_tag_name("td")[columnIndex]


def getLinkElementOfRow(rowText, linkText):
    for tableRow in tableRows:
        rowColumns = tableRow.find_elements_by_tag_name("td")
        for rowColumn in rowColumns:
            if rowColumn.text == rowText:
                linkToHighlight = tableRow.find_element_by_link_text(linkText)
                return linkToHighlight


def getTextElementOfRow(rowText):
    for tableRow in tableRows:
        rowColumns = tableRow.find_elements_by_tag_name("td")
        for rowColumn in rowColumns:
            if rowColumn.text == rowText:
                return rowColumn


def clickGreenButton():
    driver.find_element_by_css_selector("a[class='button success']").click()


if __name__ == '__main__':
    elementsToHighlight.append(getTextElementOfRowInColumn(columnName="Diceret", rowNumber=3))
    elementsToHighlight.append(getLinkElementOfRow(rowText="Apeirian7", linkText="delete"))
    elementsToHighlight.append(getLinkElementOfRow(rowText="Apeirian2", linkText="edit"))
    elementsToHighlight.append(getTextElementOfRow(rowText="Definiebas7"))
    elementsToHighlight.append(getTextElementOfRow(rowText="Iuvaret7"))
    for element in elementsToHighlight:
        highlightElement(element)
        time.sleep(2)
    clickGreenButton()