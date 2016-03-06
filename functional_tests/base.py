from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from common.models import Injection, CRI, Prescription
from treatment_sheets.models import TxSheet, TxItem

from selenium import webdriver

import sys


DEFAULT_WAIT = 10


class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_host = arg.split('=')[1]
                cls.server_url = 'http://' + cls.server_host
                cls.against_staging = True
                return
        super().setUpClass()
        cls.against_staging = False
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if not cls.against_staging:
            super().tearDownClass()

    def setUp(self):
        get_user_model().create_user(username='Marfalo', password='terriblepassword')

        Injection.objects.create(name='Tramadol', factor=1/50, concentration='5 mg/mL',
                                 category='Narcotic', admin='PO BID',
                                 desc='It can treat moderate to severe pain.')
        CRI.objects.create(name='Morphine', rates=[0.05, 0.005, 0.1, 0.001], factor=1/15, units="mg", calc_type='ez')
        CRI.objects.create(name='Dobutamine', factor=1/12500, calc_type='adv')
        Prescription.objects.create(name='Tylenol', desc='Miracle drug that cures everything.')
        Prescription.objects.create(name='Robitussin', desc='DMX')

        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.startup.homepage", "about:blank")
        profile.set_preference("startup.homepage_welcome_url", "about:blank")
        profile.set_preference("startup.homepage_welcome_url.additional", "about:blank")
        self.browser = webdriver.Firefox(firefox_profile=profile)
        self.browser.implicitly_wait(DEFAULT_WAIT)

    def tearDown(self):
        self.browser.quit()
        super().tearDown()

    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_weight')

    def login_user(self):
        self.client.login(username='Marfalo', password='terriblepassword')

    def create_list(self):
        marfalo = User.objects.get(username='Marfalo')
        tx_sheet = TxSheet.objects.create(owner=marfalo, name='DD')
        item1 = TxItem.objects.create(med=Injection.objects.get(name='Tylenol'))
        tx_sheet.item_set.add(item1)
