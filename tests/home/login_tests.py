import os

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest
import platform

class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        baseURL = 'https://letskodeit.teachable.com'

        # driver = webdriver.Chrome('/home/master/PycharmProjects/LetsCodeIt/resources/linux/chromedriver')


        os = platform.system()
        if os == "Linux":
            caps = DesiredCapabilities.FIREFOX
            caps["marionette"] = True
            caps["binary"] = "/usr/bin/firefox"
            geckodriver = "/home/master/PycharmProjects/LetsCodeIt/resources/linux/geckodriver"
            driver = webdriver.Firefox(capabilities=caps, executable_path=geckodriver)

        else:
            # # ff driver
            # caps = DesiredCapabilities.FIREFOX
            # caps["marionette"] = True
            # caps["binary"] = r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"
            # geckodriver = r"D:\projects\DRIVERS\geckodriver"
            # driver = webdriver.Firefox(capabilities=caps, executable_path=geckodriver)

            # chrome driver
            driver = webdriver.Chrome(r"D:\projects\DRIVERS\chromedriver.exe")


        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get(baseURL)

        lp = LoginPage(driver)
        lp.login("test@email.com", "abcabc" )


        userIcon = driver.find_element(By.XPATH, ".//img[@class='gravatar']")
        if userIcon is not None:
            print("login Successful")

        else:
            print ("login Failed")


