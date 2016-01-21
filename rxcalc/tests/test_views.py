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


class CalcDosageTest(TestCase):

    def test_view_returns_correct_dosage(self):
        Medication.objects.create(name='Tramadol', factor=1/50)
        response = self.client.post('/rxcalc/calc', data={'weight': 9.2})
        self.assertAlmostEqual(response.context['dosages'][0], 0.184)
