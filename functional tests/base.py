from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver

import sys


DEFAULT_WAIT = 10


class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_host = arg.split('=')[1]
                cls.server_url = 'http://' + cls.server_host
                cls.against_staging = True
                return
        super().setUpClass()
        cls.against_staging = False
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if not cls.against_staging:
            super().tearDownClass()

    def setUp(self):

        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.startup.homepage", "about:blank")
        profile.set_preference("startup.homepage_welcome_url", "about:blank")
        profile.set_preference("startup.homepage_welcome_url.additional", "about:blank")
        self.browser = webdriver.Firefox(firefox_profile=profile)
        self.browser.implicitly_wait(DEFAULT_WAIT)

    def tearDown(self):
        self.browser.quit()
        super().tearDown()

    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_inputbox')