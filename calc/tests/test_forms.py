from django.test import TestCase

from calc.forms import INVALID_INPUT_ERROR, CalcInjForm, CRISimpleForm, CRIAdvancedForm, CRICPRForm, CRIMetoclopramideForm


class CalcInjFormTest(TestCase):

    def test_form_rejects_non_numeric_input(self):
        form = CalcInjForm(data={'weight': 'a string'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['weight'], [INVALID_INPUT_ERROR])

    def test_form_rejects_empty_string(self):
        form = CalcInjForm(data={'weight': ''})
        self.assertFalse(form.is_valid())


class CRISimpleFormTest(TestCase):

    def test_form_rejects_non_numeric_input(self):
        form = CRISimpleForm(data={'weight': 'a string'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['weight'], [INVALID_INPUT_ERROR])

    def test_form_rejects_empty_string(self):
        form = CRISimpleForm(data={'weight': ''})
        self.assertFalse(form.is_valid())


class CRIAdvancedFormTest(TestCase):

    def test_form_rejects_non_numeric_input(self):
        form = CRIAdvancedForm(data={'weight': 'wait',
                                     'rate': 'eight',
                                     'vol': 'volume',
                                     'infusion': 'fusion'})
        self.assertFalse(form.is_valid())

    def test_form_rejects_empty_string(self):
        form = CRIAdvancedForm(data={'weight': '',
                                     'rate': '',
                                     'vol': '',
                                     'infusion': ''})
        self.assertFalse(form.is_valid())


class CRIInsulinFormTest(TestCase):

    def test_form_rejects_non_numeric_input(self):
        form = CRIAdvancedForm(data={'weight': 'wait',
                                     'rate': 'eight',
                                     'vol': 'volume',
                                     'replacement': 'enplacement'})
        self.assertFalse(form.is_valid())

    def test_form_rejects_empty_string(self):
        form = CRIAdvancedForm(data={'weight': '',
                                     'rate': '',
                                     'vol': '',
                                     'replacement': ''})
        self.assertFalse(form.is_valid())


class CRICPRFormTest(TestCase):

    def test_form_rejects_non_numeric_input(self):
        form = CRICPRForm(data={'weight': 'wait',
                                'rate': 'eight',
                                'vol': 'volume',
                                'dobutamine': 'nobutamine',
                                'dopamine': 'nopamine',
                                'lidocaine': 'hidocaine'})
        self.assertFalse(form.is_valid())

    def test_form_rejects_empty_string(self):
        form = CRICPRForm(data={'weight': '',
                                'rate': '',
                                'vol': '',
                                'dobutamine': '',
                                'dopamine': '',
                                'lidocaine': ''})
        self.assertFalse(form.is_valid())


class CRIMetoclopramideTest(TestCase):

    def test_form_rejects_non_numeric_input(self):
        form = CRIMetoclopramideForm(data={'weight': 'wait',
                                           'rate': 'eight',
                                           'volume': 'volume',
                                           'infusion': 'fusion',
                                           'inc_volume': 'volume',
                                           'inc_infusion': 'fusion'})
        self.assertFalse(form.is_valid())

    def test_form_rejects_empty_string(self):
        form = CRIMetoclopramideForm(data={'weight': '',
                                           'rate': '',
                                           'volume': '',
                                           'infusion': '',
                                           'inc_volume': 100,
                                           'inc_infusion': 1})
        self.assertFalse(form.is_valid())

    def test_increase_volume_and_infusion_fields_are_optional(self):
        form = CRIMetoclopramideForm(data={'weight': 4.0,
                                           'rate': 10,
                                           'volume': 100,
                                           'infusion': 4,
                                           'inc_volume': '',
                                           'inc_infusion': ''})
        self.assertTrue(form.is_valid())
