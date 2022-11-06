from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime

now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

#"""Location of screenshots"""
#SCREENSHOTS_DIR = "/home/danw32/PyCharmProjects/TestProjectVEnv/Screenshots/"


# Source: http://stackoverflow.com/questions/36936345/python-selenium-test-suite-single-webdriver-instance"""

class SeleniumTest():
    @classmethod
    def setUpClass(cls):
        """Use Chromedriver from google repo and not pip. It's newer and won't break!!"""
        # **Linux path**


        options = Options()
        options.add_argument("download.default_directory=C:\\Users")
        cls.driver = webdriver.Chrome(options=options, executable_path=r'C:\Users\91630\PycharmProjects\seleniumtest\chromedriver\chromedriver.exe')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

    # this needs to save in different directories for each line of excel sheet/every pass.
    @classmethod
    def take_screenshot_now(cls, filename):
        try:
            print ("Taking screenshot: " + filename)
            cls.driver.get_screenshot_as_file(
                'C:/Users/91630/PycharmProjects/screensht' + filename + '_' + now + '.png')
            cls.driver.implicitly_wait(10)

        except Exception as e:
            print (e)
            cls.driver.get_screenshot_as_file(
                'C:/Users/91630/PycharmProjects/screensht')