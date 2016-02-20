from django.test import TestCase

from common.models import Injection
from common.models import CRI
from calc.forms import CalcInjForm, CRISimpleForm


class InjectionTest(TestCase):

    def test_injection_page_renders_injection_page_template(self):
        response = self.client.get('/calc/injection/')
        self.assertTemplateUsed(response, 'calc/injection.html')

    def test_injection_page_passes_rx_context(self):
        med = Injection.objects.create(name='Tramadol')
        response = self.client.get('/calc/injection/')
        self.assertIn(med, list(response.context['rx'].items())[0])

    def test_injection_page_uses_form(self):
        response = self.client.get('/calc/injection/')
        self.assertIsInstance(response.context['form'], CalcInjForm)

    def test_can_unpack_zipped_rx_and_dosage(self):
        Injection.objects.create(name='Tramadol', factor=1/50)
        response = self.client.get('/calc/injection/',
                                   data={'weight': 9.2}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(list(response.context['rx'].items())[0][0], Injection.objects.first())
        self.assertAlmostEqual(list(response.context['rx'].items())[0][1], 0.184)

    def test_injection_submit_button_does_not_send_empty_string(self):
        response = self.client.get('/calc/injection/', data={'weight': ''})
        self.assertNotEqual(500, response.status_code)


class CRISimpleTest(TestCase):

    def test_cri_simple_uses_cri_simple_template(self):
        response = self.client.get('/calc/cri/simple/')
        self.assertTemplateUsed(response, 'calc/cri_simple.html')

    def test_cri_simple_calc_uses_cri_simple_form(self):
        response = self.client.get('/calc/cri/simple/')
        form = CRISimpleForm()
        self.assertIsInstance(response.context['form'], CRISimpleForm)

    def test_cri_simple_calc_only_retrieves_ez_cri(self):
        med1 = CRI.objects.create(name='Morphine', calc_type='ez')
        med2 = CRI.objects.create(name='Super Morphine', calc_type='adv')
        response = self.client.get('/calc/cri/simple/', data={'weight': 25.00})
        self.assertIn(med1, response.context['rx'])
        self.assertNotIn(med2, response.context['rx'])

    def test_cri_page_returns_correct_dosages(self):
        med = CRI.objects.create(name='Morphine', calc_type='ez', rates=[0.05, 0.5, 0.1, 1.0],
                                 factor=1/15, units='mg')
        response = self.client.get('/calc/cri/simple/', data={'weight': 25.00},
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        dosage = [(0.05, 0.083), (0.5, 0.833), (0.1, 0.167), (1.0, 1.667)]

        self.assertIn(dosage, response.context['rx'].values())

    def test_cri_simple_calc_does_not_submit_empty_strings(self):
        response = self.client.get('/calc/cri/simple/', data={'weight': ''})
        self.assertNotEqual(500, response.status_code)
