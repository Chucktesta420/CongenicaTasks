from features.browser import Browser
from helpers.page_objects.EventsPage import EventsPage
from helpers.page_objects.LoginPage import LoginPage
from helpers.page_objects.SearchPage import SearchPage
from helpers.page_objects.SectorsPage import SectorsPage


def before_all(context):
    context.browser = Browser()
    context.searchPage = SearchPage()
    context.loginPage = LoginPage(context.browser)
    context.sectorsPage = SectorsPage(context.browser)
    context.eventsPage = EventsPage(context.browser)


def after_all(context):
    context.browser.quit()
