"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import os
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        baseURL = "https://letskodeit.teachable.com/"


        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie(r"D:\projects\DRIVERS\MicrosoftWebDriver.exe")
        elif self.browser == "firefox":
            # Set ff driver
            caps = DesiredCapabilities.FIREFOX
            caps["marionette"] = True
            caps["binary"] = r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"
            geckodriver = r"D:\projects\DRIVERS\geckodriver"
            driver = webdriver.Firefox(capabilities=caps, executable_path=geckodriver)
        elif self.browser == "chrome":
            # Set chrome driver
            chromedriver = r"D:\projects\DRIVERS\chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = chromedriver
            driver = webdriver.Chrome(chromedriver)

        else:
            driver = webdriver.Chrome(r"D:\projects\DRIVERS\chromedriver.exe")
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(15)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver

