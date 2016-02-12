from django.test import TestCase
from django.utils.html import escape

from rxcalc.models import Medication
from rxcalc.forms import WeightForm


class HomePageTest(TestCase):

    def test_home_page_renders_home_page_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'rxcalc/home.html')

    def test_view_sets_active_class_on_link(self):
        response = self.client.get('/')
        self.assertEqual('home', response.context['navbar'])


class CalcPageTest(TestCase):

    def test_home_page_renders_calc_page_template(self):
        response = self.client.get('/rxcalc/calc/')
        self.assertTemplateUsed(response, 'rxcalc/calc.html')

    def test_home_page_passes_rx_context(self):
        med = Medication.objects.create(name='Tramadol')
        response = self.client.get('/rxcalc/calc/')
        self.assertIn(med, list(response.context['rx'].items())[0])

    def test_home_page_uses_form(self):
        response = self.client.get('/rxcalc/calc/')
        self.assertIsInstance(response.context['form'], WeightForm)

    def test_can_unpack_zipped_rx_and_dosage(self):
        Medication.objects.create(name='Tramadol', factor=1/50)
        response = self.client.post('/rxcalc/calc/', data={'weight': 9.2})
        self.assertEqual(list(response.context['rx'].items())[0][0], Medication.objects.first())
        print
        self.assertAlmostEqual(list(response.context['rx'].items())[0][1], 0.184)

    def test_calc_submit_button_does_not_send_empty_string(self):
        response = self.client.post('/rxcalc/calc', data={'weight': ''})
        self.assertNotEqual(500, response.status_code)


class InfoPageTest(TestCase):

    def test_info_page_renders_info_page_template(self):
        response = self.client.get('/rxcalc/info/')
        self.assertTemplateUsed(response, 'rxcalc/info.html')

    def test_info_page_displays_all_medications(self):
        tram = Medication.objects.create(name='Tramadol')
        ampi = Medication.objects.create(name='Ampicillin')
        response = self.client.get('/rxcalc/info/')
        self.assertIn(tram, response.context['meds'])
        self.assertIn(ampi, response.context['meds'])


class RxInfoPageTest(TestCase):

    def test_rx_page_url_corresponds_to_rx_slug(self):
        med = Medication.objects.create(name='Super Tramadol (Nighttime)')
        response = self.client.get('/rxcalc/info/{}/'.format(med.slug))
        self.assertEqual(200, response.status_code)

    def test_rx_info_renders_rx_info_template(self):
        Medication.objects.create(name='Super Tramadol Nighttime')
        response = self.client.get('/rxcalc/info/super-tramadol-nighttime/')
        self.assertTemplateUsed(response, 'rxcalc/rx.html')
