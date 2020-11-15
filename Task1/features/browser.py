import os

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Browser():
    chromedriverPath = os.path.join(os.get_exec_path()[0], "..\\..\\helpers\\chromedriver.exe")
    driver = webdriver.Chrome(executable_path=chromedriverPath)
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()

    def quit(context):
        context.driver.quit()