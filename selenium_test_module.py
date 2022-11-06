import time
from selenium.webdriver.common.keys import Keys
import driverglobal
import logging

logging.basicConfig(filename='example.log',level=logging.INFO)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')


class SeleniumClass(driverglobal.SeleniumTest):
    """this is just to test stuff out"""

    def setUp(self):
        self.setUpClass()

    def go_to_url(self, url):
        self.driver.get(url)
        self.take_screenshot_now("from_sel_test_mod")
        logging.info("Screenshot Taken")

    def teardown(self):
        self.tearDownClass()

    """***This is the main one to use***"""

    # def test_selenium_code_lottery(self, url_val, username, password):
    def test_selenium_code_lottery(self, url_val, username, password, first_number, second_number):
        try:
            self.setUpClass()
            self.driver.get(url_val)
            self.driver.implicitly_wait(10)

            """This works - had to change the double quotes on id='header' to single ones"""
            if self.driver.find_element_by_xpath("//*[@id='header']/div/nav[1]/div[2]/div[5]/div").is_displayed():
                self.driver.find_element_by_xpath(
                    "// *[ @ id = 'header'] / div / nav[1] / div[2] / div[4] / div / div").click()

            self.driver.find_element_by_id("username").clear()
            self.driver.find_element_by_id("username").send_keys(username)
            self.driver.find_element_by_id("password").clear()
            self.driver.find_element_by_id("password").send_keys(password)
            self.take_screenshot_now("sign_in_page")
            self.driver.find_element_by_id("password").send_keys(Keys.ENTER)
            # self.driver.find_element_by_css_selector("button.button").click()

            # need assert before screenshot, and the implicit wait.

            #### Wack some logging in after every screenshot for future HTML report
            #### Also some asserts of driver title etc.

            self.driver.implicitly_wait(10)
            self.take_screenshot_now("signed_in")
            # Click Lotto link at top of homepage
            self.driver.find_element_by_xpath(
                "//header[@id='header']/div/nav/div/div/a[8]/div").click()
            time.sleep(5)

            """This is the low deposit box that pops up - this if stmt makes it go away"""
            if self.driver.find_element_by_id("myModalLabel").is_displayed():
                self.driver.find_element_by_id("button1").click()

            """Click Irish Lottery link on lotto homepage"""
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_xpath(
                "//div[@class='irish lotto-btn-launch']/span[@class='hp-choose-lotto-title']").click()

            """Click lotto irish 6 ball button (hard wait works better atm. Explicit waits are a faff)."""
            time.sleep(3)
            self.driver.find_element_by_xpath(
                "//*[@id='content-section-main']/div[1]/div[2]/ng-view/div/div[2]/div[1]/div[2]/div[1]/a/button").click()


            self.driver.implicitly_wait(10)

            # using neighbour xpath from Katalon
            self.driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Wednesday 1st draw (Main)'])[1]/preceding::input[1]").click()

            self.driver.implicitly_wait(10)
            self.take_screenshot_now("lottery")


            self.driver.find_element_by_id("lottos-straight-" + first_number).click()
            time.sleep(2)
            # self.driver.find_element_by_id("lottos-straight-32").click()
            self.driver.find_element_by_id("lottos-straight-" + second_number).click()
            self.take_screenshot_now("lottery_numbers")



            # sleep just to check everything is good before closing
            time.sleep(3)
            self.tearDownClass()

        except Exception as e:
            print (e)
            # now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            # self.driver.get_screenshot_as_file('failure-%s.png' % now)
            self.take_screenshot_now("test_failure")
            self.tearDownClass()