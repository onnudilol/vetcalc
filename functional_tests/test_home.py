from .base import FunctionalTest

from selenium.webdriver.common.keys import Keys


class HomePageTest(FunctionalTest):

    def test_home_page_displays_menu(self):
        # Marfalo the vet tech is sick of calculating dosages by hand and is too lazy to use a spreadsheet,
        # so he decides to use a web app.
        # Marfalo finds VeTeCalc on the search engine of his choice and clicks on the link.
        self.browser.get(self.server_url)
        self.assertIn('VeTeCalc', self.browser.title)

        # Marfalo sees that there is a page to calculate dosages, get information about commonly used drugs,
        # and a page to create a treatment sheet
        # These should not raise #
        self.browser.find_element_by_link_text('Calculate Dosages')
        self.browser.find_element_by_link_text('Rx Info')
        self.browser.find_element_by_link_text('Create A Treatment Sheet')

    def test_navbar_updates_active_class(self):
        # Marfalo clicks on a link and sees that the navigation bar updates to show what page he is on
        self.browser.get(self.server_url)
        self.browser.find_element_by_link_text('Calc').send_keys(Keys.RETURN)
        active = self.browser.find_element_by_xpath("//li[@class='active']/a[1]")
        self.assertIn('Calc', active.text)

        # Marfalo is done calculating dosages and returns to the home page
        # When he does, the navbar updates to show that he is back on the home page
        navbar_home = self.browser.find_element_by_link_text('Home')
        navbar_home.send_keys(Keys.RETURN)
        active = self.browser.find_element_by_xpath("//li[@class='active']/a[1]")
        self.assertIn('Home', active.text)
