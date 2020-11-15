from behave import *

use_step_matcher("re")
# chromedriverPath = os.path.join(os.get_exec_path()[0], "..\\..\\helpers\\chromedriver.exe")
# driver = webdriver.Chrome(executable_path=chromedriverPath)

# Login credentials
email = "robotuintelektoregistracija@gmail.com"
password = "RobotsIntellect123!"


@given('I go to "https://www\.tiketa\.lt/EN/search"')
def step_impl(context):
    context.searchPage.goToPage()
    context.searchPage.driver.maximize_window()


@step("Login into my account")
def step_impl(context):
    if context.searchPage.isUserLoggedIn() == False:
        loginPage = context.searchPage.goToLoginPage()
        loginPage.login(email, password)


@when("I search (?P<caption>.+)")
def step_impl(context, caption):
    context.searchPage.goToPage()
    context.searchPage.enterSearchField(caption)


@step("Select (?P<cityName>.+) city")
def step_impl(context, cityName):
    context.searchPage.selectCity(cityName)


@step("Choose dates from (?P<dateFrom>.+) to (?P<dateTo>.+)")
def step_impl(context, dateFrom, dateTo):
    context.searchPage.enterDateFrom(dateFrom)
    context.searchPage.enterDateTo(dateTo)


@step("Click search button")
def step_impl(context):
    context.searchPage.clickSearchButton()


@step("Click (?P<event>.+) buy button")
def step_impl(context, event):
    context.eventsPage = context.searchPage.clickBuyEventButton(event)


@step("Select (?P<event>.+) event name with (?P<price>.+) price")
def step_impl(context, event, price):
    context.sectorsPage = context.eventsPage.clickBuyEventTicketButton(eventName=event, eventPrice=price)


@step("Select (?P<sector>.+) sector")
def step_impl(context, sector):
    context.sectorsPage.clickSectorButton(sectorName=sector)


@then("I have selected a sector")
def step_impl(context):
    return True
