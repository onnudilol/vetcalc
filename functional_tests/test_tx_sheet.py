from .base import FunctionalTest

from selenium.webdriver.common.keys import Keys

import time


class TreatmentSheetTest(FunctionalTest):

    def login_user(self):
        self.browser.get(self.server_url + '/tx_sheet/')
        self.browser.find_element_by_link_text('log in').send_keys(Keys.RETURN)
        self.browser.find_element_by_id('id_login').send_keys('Marfalo')
        self.browser.find_element_by_id('id_password').send_keys('terriblepw')
        self.browser.find_element_by_class_name('btn').send_keys(Keys.RETURN)

    def test_creating_new_treatment_sheet(self):
        # Dr. T is worried about liability so he is making the techs
        # have the clients sign one thousand pages of paperwork for every procedure.
        # This is disruptive to their workflow and highly repetitive.
        # Marfalo checks VetCalc for solution to his ennui.
        # Fortuitously, the dev has implemented a treatment sheet creator.

        # The page asks Marfalo to authenticate.  Marfalo goes through the process of registration, and is redirected
        # back to this page.  It says that he has not created any treatment sheets and invites him to do so.
        self.login_user()
        self.browser.find_element_by_link_text('Create a new treatment sheet').send_keys(Keys.RETURN)

        # The page displays a form asking for a name, choice of medication, number of units per dose,
        # and frequency of dose.
        self.browser.find_element_by_id('id_name').send_keys('Partario')
        self.browser.find_element_by_id('id_comment').send_keys('Got neutered')
        self.browser.find_element_by_id('id_med').send_keys('t')
        self.browser.find_element_by_id('id_dose').send_keys('5')
        self.browser.find_element_by_id('id_freq').send_keys('s')
        self.browser.find_element_by_id('id_unit').send_keys('m')
        self.browser.find_element_by_class_name('btn').send_keys(Keys.RETURN)

        # Marfalo is redirected to a page that displays the current treatment sheet and all its items.
        instructions = self.browser.find_element_by_class_name('content')
        self.assertIn('Take 5.0 mLs of Tylenol once a day.', instructions.text)

    def test_edit_existing_list(self):
        self.login_user()
        self.create_list()

        # Marfalo wants to add another drug to the treatment sheet, so he clicks on the link to do so.
        self.browser.find_element_by_link_text('DD: i heart diamond dogs').send_keys(Keys.RETURN)

        # The page displays a form similar to the new list page.  Marfalo adds the item he needs.
        self.browser.find_element_by_id('id_med').send_keys('r')
        self.browser.find_element_by_id('id_dose').send_keys('3')
        self.browser.find_element_by_id('id_freq').send_keys('s')
        self.browser.find_element_by_id('id_unit').send_keys('c')
        self.browser.find_element_by_class_name('btn').send_keys(Keys.RETURN)

        # He is redirected to the list page, which now displays the item he just added.
        instructions = self.browser.find_element_by_class_name('content')
        self.assertIn('Take 3.0 capsules of Robitussin once a day', instructions.text)

        # Marfalo changes his mind and decides to delete the item he just added
        self.browser.get(self.server_url + '/tx_sheet/1/2/del')
        time.sleep(5)
        no_instructions = self.browser.find_element_by_class_name('content')
        self.assertNotIn('Take 3.0 capsules of Robitussin once a day', no_instructions.text)

        # Marfalo changes his mind again and decides to delete the whole list
        self.browser.get(self.server_url + '/tx_sheet/1/del')
        no_list = self.browser.find_element_by_class_name('content')
        self.assertNotIn('DD: i heart diamond dogs', no_list.text)
