from .base import FunctionalTest

from unittest import skip


class CalcPageTest(FunctionalTest):

    def test_calc_page_accepts_input(self):
        # Dr. T is very upset.  He screams at Marfalo to prepare medication for a 12 lb dog.
        # Glancing through, he sees that the calc page displays several common medications used at the dog hospital.
        # He notices an input box to enter in the weight of the pet.
        self.browser.get(self.server_url + '/rxcalc/calc')
        self.assertEqual('Rx Calculator - VetCalc', self.browser.title)

        inputbox = self.get_item_input_box()
        inputbox.send_keys('9.2\n')

        # The page accepts his input and spits out the expected values.
        # The information includes the Rx name and concentration.
        tram = self.browser.find_element_by_id('med_1')
        self.assertIn('0.184', tram.text)
        self.assertIn('Tramadol', tram.text)
        self.assertIn('5 mg/mL', tram.text)

    @skip('stub')
    def test_can_switch_between_metric_and_imperial(self):
        # Marfalo is fed up with Dr. T's nonsense, and decides to quit and work at a dog hospital in Luxembourg.
        # Because he is an ignorant American that cannot use metric, he uses VeTeCalc to convert the values for him.
        # He clicks on radio buttons to switch the units from imperial to metric.
        pass
