from django.test import TestCase
from django.utils.html import escape

from rxcalc.models import Medication
from rxcalc.forms import WeightForm


class HomePageTest(TestCase):

    def test_home_page_renders_home_page_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'rxcalc/home.html')

    def test_home_page_passes_rx_context(self):
        med = Medication.objects.create(name='Tramadol')
        response = self.client.get('/')
        self.assertIn(med, response.context['rx'])

    def test_home_page_uses_form(self):
        response = self.client.get('/')
        response = self.assertIsInstance(response.context['form'], WeightForm)

    def test_can_unpack_zipped_rx_and_dosage(self):
        Medication.objects.create(name='Tramadol', factor=1/50)
        response = self.client.post('/rxcalc/calc', data={'weight': 9.2})
        self.assertEqual(response.context['rx'][0][0], Medication.objects.first())
        self.assertAlmostEqual(response.context['rx'][0][1], 0.184)

    def test_invalid_input_displays_error(self):
        pass
