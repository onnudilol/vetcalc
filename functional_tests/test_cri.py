from .base import FunctionalTest

import time

from selenium.webdriver.common.keys import Keys


class CRITest(FunctionalTest):

    def test_simple_cri_page(self):
        # A client has brought in their dogs that got into a fight over a piece of chocolate and then
        # both of them got hit by a car.  It is an emergency and Marfalo needs to prepare IV fluids for them.
        # By serendipitous coincidence the dev of VetCalc has just implemented this feature.
        self.browser.get(self.server_url + '/calc/cri/')

        # The CRI page displays options for simple and advanced calculations.  Marfalo only needs to prepare morphine,
        # so he chooses the simple calculator.
        self.browser.find_element_by_link_text('Simple').send_keys(Keys.RETURN)

        # The page has an input box for weight.  Marfalo calculates the CRI dosage for an 11 kg dog.
        inputbox = self.get_kg_item_input_box()
        inputbox.send_keys('25\n')

        # The page updates and displays a table with the calculated dosages.
        time.sleep(5)
        calc_cri = self.browser.find_element_by_xpath("//tbody/tr/td[2]")
        self.assertAlmostEqual('0.083', calc_cri)

    def test_advanced_cri_page(self):
        # The operation to save the dogs has gone pear shaped and one of the dogs is undergoing heart failure.
        # Dr. T is shitting his pants and screams at Marfalo to prepare dobutamine.
        # Marfalo doesn't know what that is or what it does but luckily VetCalc has a page for that.
        # This time Marfalo uses the advanced calculator.
        self.browser.get(self.server_url + '/calc/cri/')
        self.browser.find_element_by_link_text('Advanced').send_keys(Keys.RETURN)

        # Marfalo sees an input box for weight, desired fluid rate, volume of remaining fluids, and desired
        # unit/kg/time infusion.
        # Marfalo inputs the relevant information.
        self.browser.find_element_by_id('id_weight').send_keys(7)
        self.browser.find_element_by_id('id_fluid_rate').send_keys(3)
        self.browser.find_element_by_id('id_volume').send_keys(250)
        self.browser.find_element_by_id('id_infusion').send_keys(5)
        self.browser.find_element_by_class_name('btn').send_keys(Keys.RETURN)

        # The page returns a paragraph explaining how much dobutamine to add to the IV bag and at what rate the fluid
        # and infusion will be administered
        calc_cri_adv = self.browser.find_element_by_css_selector('span')
        self.assertIn('14.000', calc_cri_adv)
        self.assertIn('5.000', calc_cri_adv)

    def test_post_cpr_calc(self):
        # Marfalo has resuscitated the dogs with mouth to mouth CPR.
        # Marfalo follows up with more drugs in the IV fluids.
        self.browser.get(self.server_url + '/calc/cri/')
        self.browser.find_element_by_link_text('Post CPR').send_keys(Keys.RETURN)

        # This page is similar to the advanced CRI calculator, but has additional fields for dobutamine, dopamine,
        # and lidocaine.
        self.browser.find_element_by_id('id_weight').send_keys(0.5)
        self.browser.find_element_by_id('id_fluid_rate').send_keys(1)
        self.browser.find_element_by_id('id_volume').send_keys(10)
        self.browser.find_element_by_id('id_dobutamine').send_keys(4)
        self.browser.find_element_by_id('id_dopamine').send_keys(3)
        self.browser.find_element_by_id('id_lidocaine').send_keys(60)
        self.browser.find_element_by_class_name('btn').send_keys(Keys.RETURN)

        # The page spews out the calculated dosages
        cri_cpr_calc = self.browser.find_element_by_css_selector('p')
        values = ['0.100', '0.020', '0.900', '0.300']

        for value in values:
            self.assertIn(value, cri_cpr_calc)

    def test_metoclopramide_calc(self):
        # All the drugs that were administered have made the dogs puke.  Dr. T prescribes more drugs to fix the problem.
        # Marfalo needs to prepare metoclopramide.
        self.browser.get(self.server_url + '/calc/cri/')
        self.browser.find_element_by_link_text('Metoclopramide').send_keys(Keys.RETURN)

        # This page is similar to the advanced calculator, but has extra inputs for increasing the dosage.
        self.browser.find_element_by_id('id_weight').send_keys(4.0)
        self.browser.find_element_by_id('id_fluid_rate').send_keys(10)
        self.browser.find_element_by_id('id_volume').send_keys(100)
        self.browser.find_element_by_id('id_infusion').send_keys(4)
        self.browser.find_element_by_class_name('btn').send_keys(Keys.RETURN)

        # The numbers check out.
        cri_metoclopramide_calc = self.browser.find_element_by_css_selector('p')
        self.assertIn(0.067, cri_metoclopramide_calc)
        self.assertIn(1.33, cri_metoclopramide_calc)

        # The dogs are still puking, so Marfalo needs to increase the dosage.
        self.browser.find_element_by_id('id_inc_fluid_remaining').send_keys(100)
        self.browser.find_element_by_id('id_inc_vol_metoclopramide').send_keys(1)
        self.browser.find_element_by_class_name('btn').send_keys(Keys.RETURN)

        # The dosages are updated.
        cri_metoclopramide_inc_calc = self.browser.find_element_by_css_selector('p')
        self.assertIn(0.2, cri_metoclopramide_inc_calc)
        self.assertIn(4.5, cri_metoclopramide_inc_calc)
