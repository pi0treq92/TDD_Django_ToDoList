from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import time
import unittest


class GuestTest(LiveServerTestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        self.browser = webdriver.Chrome(options=options,
                                        executable_path=r'C:\Users\pmigdals\AppData\Local\Programs\Python\Python37\chromedriver.exe')

    def tearDown(self):
        self.browser.quit()

    def _test_check_title(self):
        self.browser.get(self.live_server_url)
        self.assertIn('To-Do', self.browser.title)
        inputbox = self.browser.find_element_by_id('inputbox_id')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Type to-do')
        inputbox.send_keys('Zaplac rachunek')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)
        tab = self.browser.find_element_by_id('table_id')
        row = tab.find_elements_by_tag_name('tr')
        self.assertIn('1: Zaplac rachunek', [r.text for r in row])
        # self.fail('Finish the test!')

    def _test_multiple_users_lists_urls_check(self):
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('inputbox_id')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        first_user_list = self.browser.current_url
        #self.assertRegex(first_user_list, 'lists/.+')
        self.browser.quit()
        self.browser = webdriver.Chrome()
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('inputbox_id')
        inputbox.send_keys('Buy chocolate')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        second_user_list = self.browser.current_url
        #self.assertRegex(second_user_list, 'lists/.+')
        self.assertNotEqual(first_user_list, second_user_list)

    def test_layout(self):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)
        inputbox = self.browser.find_element_by_id('inputbox_id')
        self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width']/2, 512, delta=10)


if __name__ == '__main__':
    unittest.main(warnings='ignore')