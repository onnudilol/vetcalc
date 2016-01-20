from django.test import TestCase
from django.utils.html import escape

from rxcalc.models import Medication
from rxcalc.forms import INVALID_INPUT_ERROR


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
        response = self.assertIn(response.context['form'], WeightInputForm)

    def test_home_page_displays_form_errors(self):
        response = self.client.post('/', data={'weight': 'eleven'})
        self.assertContains(response, escape(INVALID_INPUT_ERROR))
