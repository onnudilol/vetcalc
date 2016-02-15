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
        self.assertEqual('Tramadol - VetCalc', self.browser.title)

        # The url of the page is the slug of the medication name
        self.assertEqual(self.browser.current_url, self.server_url + '/rxcalc/info/tramadol')
