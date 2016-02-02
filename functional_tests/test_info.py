from .base import FunctionalTest

from selenium.webdriver.common.keys import Keys


class RxInfoPageTest(FunctionalTest):

    def test_rx_info_page_displays_rx_info(self):
        # Marfalo is asked to explain medications to a client.
        # He shits his pants because he has no idea what any of them are or what they do.
        # Fortuitously, the developer of VeTeCalc has implemented a page that displays useful rx info.
        # Marfalo opens up the page.

        self.browser.get(self.server_url + '/rxcalc/info/')

        # It displays a lists of medications much like the calc page.
        # Clicking on the name of a medication links to a page for the medication
        # that displays more detailed information.

        self.browser.find_element_by_link_text('Tramadol').send_keys(Keys.RETURN)
        self.assertEqual('Tramadol - VeTeCalc', self.browser.title)

        # The url of the page is the slug of the medication name
        self.assertEqual(self.server_url + '/rxcalc/info')

        # The page displays specific information on a sidebar on the left
        column = self.browser.find_element_by_css_selector('.left-column').find_element_by_tag_name('h1')
        self.assertEqual('Tramadol', column.text)

        column_sections = self.browser.find_element_by_css_selector('.left-column').find_elements_by_tag_name('h2')
        for section in ['Category', 'Administration']:
            self.assertIn(section, column_sections)

        # The rest of the page displays a detailed description of what the medication is and what it is used for.
        tram_desc = self.browser.find_element_by_css_selector('.rx-info')
        self.assertIn('It can treat moderate to severe pain.', tram_desc)
