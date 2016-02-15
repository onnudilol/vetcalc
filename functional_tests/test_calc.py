from .base import FunctionalTest

from unittest import skip
import time


class CalcPageTest(FunctionalTest):

    def test_calc_page_accepts_input(self):

        # Dr. T is very upset.  He screams at Marfalo to prepare medication for a 12 lb dog.
        # Glancing through, he sees that the calc page displays several common medications used at the dog hospital.
        # He notices an input box to enter in the weight of the pet.
        self.browser.get(self.server_url + '/rxcalc/calc')
        self.assertEqual('Injection Calculator - VetCalc', self.browser.title)

        inputbox = self.get_item_input_box()
        inputbox.send_keys('9.2\n')

        # The page accepts his input and spits out the expected values.
        # The information includes the Rx name and concentration.
        # (time.sleep() is lame, need to find a better way to handle ajax
        time.sleep(5)
        tram = self.browser.find_elements_by_tag_name('td')
        self.assertIn('Tramadol', tram[0].text)
        self.assertIn('0.184', tram[1].text)
        self.assertIn('5 mg/mL', tram[2].text)

    @skip('stub')
    def test_can_switch_between_metric_and_imperial(self):
        # Marfalo is fed up with Dr. T's nonsense, and decides to quit and work at a dog hospital in Luxembourg.
        # Because he is an ignorant American that cannot use metric, he uses VeTeCalc to convert the values for him.
        # He clicks on radio buttons to switch the units from imperial to metric.
        pass
