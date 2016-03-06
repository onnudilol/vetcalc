from .base import FunctionalTest

from selenium.webdriver.common.keys import Keys


class TreatmentSheetTest(FunctionalTest):

    def test_creating_new_treatment_sheet(self):
        # Dr. T is worried about liability so he is making the techs
        # have the clients sign one thousand pages of paperwork for every procedure.
        # This is disruptive to their workflow and highly repetitive.
        # Marfalo checks VetCalc for solution to his ennui.
        # Fortuitously, the dev has implemented a treatment sheet creator.
        self.browser.get(self.server_url + '/calc/tx_sheet/')

        # The page asks Marfalo to authenticate.  Marfalo goes through the process of registration, and is redirected
        # back to this page.  It says that he has not created any treatment sheets and invites him to do so.
        self.login_user()
        self.browser.find_element_by_link_text('Create a new treatment sheet').send_keys(Keys.RETURN)

        # The page displays a form asking for a name, choice of medication, number of units per dose,
        # and frequency of dose.
        self.browser.find_element_by_id('id_name').send_keys('Partario')
        self.browser.find_element_by_id('id_rx_choice').send_keys('Tylenol\n')
        self.browser.find_element_by_id('id_dose_units').send_keys('5')
        self.browser.find_element_by_id('id_dose_freq').send_keys('MLBID\n')
        self.browser.find_element_by_class_name('btn').send_keys(Keys.RETURN)

        # Marfalo is redirected to a page that displays the current treatment sheet and all its items.
        drugs = self.browser.find_elements_by_class_name('rx_item')
        self.assertIn('Take 5 mL of Tylenol twice a day', drugs[0].text)

    def test_edit_existing_list(self):
        self.login_user()
        self.create_list()

        # Marfalo wants to add another drug to the treatment sheet, so he clicks on the link to do so.
        self.browser.find_element_by_link_text('Add another item').send_keys(Keys.RETURN)

        # The page displays a form similar to the new list page.  Marfalo adds the item he needs.
        self.browser.find_element_by_id('id_rx_choice').send_keys('Robitussin\n')
        self.browser.find_element_by_id('id_dose_units').send_keys('3')
        self.browser.find_element_by_id('id_dose_freq').send_keys('CSID\n')
        self.browser.find_element_by_class_name('btn').send_keys(Keys.RETURN)

        # He is redirected to the list page, which now displays the item he just added.
        drugs = self.browser.find_elements_by_class_name('rx_item')
        self.assertIn('Take 3 capsules of Robitussin once a day', drugs[1].text)

        # Marfalo changes his mind and decides to delete the item he just added
        removed_item = self.browser.find_elements_by_link_text('Remove item')[1].send_keys(Keys.RETURN)
        self.assertNotIn('Robitussin', removed_item.text)
