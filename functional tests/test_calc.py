from .base import FunctionalTest

from selenium.webdriver.common.keys import Keys

from unittest import skip

from rxcalc.dosage import DOSAGE_INJECTION


class HomePageTest(FunctionalTest):

    def test_home_page_displays_rx_info(self):
        # Marfalo the vet tech is sick of calculating dosages by hand and is too lazy to use a spreadsheet,
        # so he decides to use a web app.
        # Marfalo finds VeTeCalc on the search engine of his choice and clicks on the link.
        self.browser.get(self.server_url)
        self.assertIn('VeTeCalc', self.browser.title)

        # Glancing through, he sees that the home page displays several common medications used at the dog hospital.
        # The information includes the Rx name and concentration.

    def test_home_page_accepts_input(self):
        # Dr. T is very upset.  He screams at Marfalo to prepare medication for a 12 lb dog.
        # He notices an input box to enter in the weight of the pet.
        inputbox = self.get_item_input_box()
        inputbox.send_keys('12\n')

        # The page accepts his input and spits out the expected values.
        ampi = self.browser.find_element_by_id('id_ampicillin')
        ampi_dosage = ampi.find_element_by_class_name('dosage')
        self.assertIn(ampi_dosage, '0.2')

    @skip
    def test_can_switch_between_metric_and_imperial(self):
        # Marfalo is fed up with Dr. T's nonsense, and decides to quit and work at a dog hospital in Luxembourg.
        # Because he is an ignorant American that cannot use metric, he uses VeTeCalc to convert the values for him.
        # He clicks on radio buttons to switch the units from imperial to metric.
        pass
