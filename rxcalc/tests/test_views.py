from django.test import TestCase
from django.utils.html import escape

from rxcalc.models import Medication
from rxcalc.forms import WeightForm


class HomePageTest(TestCase):

    def test_view_sets_active_class_on_link(self):
        response = self.client.get('/')
        self.assertEqual('home', response.context['navbar'])


class CalcPageTest(TestCase):

    def test_home_page_renders_home_page_template(self):
        response = self.client.get('/rxcalc/calc/')
        self.assertTemplateUsed(response, 'rxcalc/calc.html')

    def test_home_page_passes_rx_context(self):
        med = Medication.objects.create(name='Tramadol')
        response = self.client.get('/rxcalc/calc/')
        self.assertIn(med, response.context['rx'][0])

    def test_home_page_uses_form(self):
        response = self.client.get('/rxcalc/calc/')
        response = self.assertIsInstance(response.context['form'], WeightForm)

    def test_can_unpack_zipped_rx_and_dosage(self):
        Medication.objects.create(name='Tramadol', factor=1/50)
        response = self.client.post('/rxcalc/calc/', data={'weight': 9.2})
        self.assertEqual(response.context['rx'][0][0], Medication.objects.first())
        self.assertAlmostEqual(response.context['rx'][0][1], 0.184)
