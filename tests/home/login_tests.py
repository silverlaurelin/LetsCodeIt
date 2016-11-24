
from pages.home.login_page import LoginPage
import unittest
import pytest
from utilities.stats import Status


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyTitle()
        self.ts.mark(result1, "Title Verified")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login was successful")

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("test@email.com", "abcabcabc")
        result = self.lp.verifyLoginFailed()
        self.ts.mark(result, "Login Fail Verified")


# os = platform.system()
# if os == "Linux":
#     # ff driver
#     caps = DesiredCapabilities.FIREFOX
#     caps["marionette"] = True
#     caps["binary"] = "/usr/bin/firefox"
#     geckodriver = "/home/master/PycharmProjects/LetsCodeIt/resources/linux/geckodriver"
#     driver = webdriver.Firefox(capabilities=caps, executable_path=geckodriver)
#     # #chrome driver
#     # driver = webdriver.Chrome('/home/master/PycharmProjects/LetsCodeIt/resources/linux/chromedriver')
#
# else:
#     ## ff driver
#     # caps = DesiredCapabilities.FIREFOX
#     # caps["marionette"] = True
#     # caps["binary"] = r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"
#     # geckodriver = r"D:\projects\DRIVERS\geckodriver"
#     # driver = webdriver.Firefox(capabilities=caps, executable_path=geckodriver)
#
#     # chrome driver
#     driver = webdriver.Chrome(r"D:\projects\DRIVERS\chromedriver.exe")
#
# driver.maximize_window()
# driver.implicitly_wait(30)
# driver.get(baseURL)

