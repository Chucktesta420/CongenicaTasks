from features.browser import Browser


class LoginLocators():
    usernameFieldId = "txtLoginName"
    passwordFieldId = "txtLoginPsw"
    loginButtonId = "btnLogin"


class LoginPage():
    def __init__(self, driver):
        # Login information
        self.driver = driver
        self.email = "robotuintelektoregistracija@gmail.com"
        self.password = "RobotsIntellect123!"

    def login(self, username, password):
        usernmaeField = self.driver.find_element_by_id(LoginLocators.usernameFieldId)
        passwordField = self.driver.find_element_by_id(LoginLocators.passwordFieldId)
        usernmaeField.send_keys(username)
        passwordField.send_keys(password)
        self.clickLoginButton()

    def clickLoginButton(self):
        loginButton = self.driver.find_element_by_id(LoginLocators.loginButtonId)
        loginButton.click()