from django.test import TestCase

from common.models import Injection
from calc.forms import WeightForm


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
        self.assertIsInstance(response.context['form'], WeightForm)

    def test_can_unpack_zipped_rx_and_dosage(self):
        Injection.objects.create(name='Tramadol', factor=1/50)
        response = self.client.get('/calc/injection/',
                                   data={'weight': 9.2}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(list(response.context['rx'].items())[0][0], Injection.objects.first())
        self.assertAlmostEqual(list(response.context['rx'].items())[0][1], 0.184)

    def test_injection_submit_button_does_not_send_empty_string(self):
        response = self.client.post('/calc/injection/', data={'weight': ''})
        self.assertNotEqual(500, response.status_code)


class CRISimpleTest(TestCase):

    def test_cri_simple_uses_cri_simple_template(self):
        response = self.client.get('/calc/cri/')
        self.assertTemplateUsed(response, 'calc/cri.html')

    def test_cri_page_(self):
        pass

