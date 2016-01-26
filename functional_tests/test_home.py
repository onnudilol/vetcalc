from .base import FunctionalTest


class HomePageTest(FunctionalTest):

    def test_home_page_displays_rx_info(self):
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
