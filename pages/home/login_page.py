import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    #locators
    _login_link =  ".//a[@class='navbar-link fedora-navbar-link']"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")


    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent(locator="//div[@id='navbar']//li[@class='dropdown']", locatorType="xpath" )
        return result


    def verifyLoginFailed(self):
        result = self.isElementPresent(".//div[@class='alert alert-danger' and contains(text(), 'Invalid email or password')]", locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Let's Kode It")

    def logOut(self):
        self.nav.navigateToUserSettings()
        logoutLinkElement = self.waitForElement(locator="//div[@id='navbar']//a[@href='/sign_out']",
                                                locatorType="xpath", pollFrequency=3)
        self.elementClick(element=logoutLinkElement)
