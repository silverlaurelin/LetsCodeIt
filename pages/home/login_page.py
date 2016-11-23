from selenium.webdriver.common.by import By

from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        #locators
    _login_link_ =  ".//a[@class='navbar-link fedora-navbar-link']"
    _email_field_ = "user_email"
    _password_field_ = "user_password"
    _login_button_ = "commit"

    def getLoginLink(self):
        return self.driver.find_element(By.XPATH, self._login_link_)

    def getEmailField(self):
        return self.driver.find_element(By.ID, self._email_field_)

    def getPasswordField(self):
        return self.driver.find_element(By.ID, self._password_field_)

    def getLoginButton(self):
        return  self.driver.find_element(By.NAME, self._login_button_)



    def clickLoginLink(self):
        self.getLoginLink().click()

    def enterEmail(self, email):
        self.getEmailField().send_keys(email)

    def enterPassword(self, password):
        self.getPasswordField().send_keys(password)

    def clickLoginButton(self):
        self.getLoginButton().click()


    def login(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()


