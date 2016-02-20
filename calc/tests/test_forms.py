from django.test import TestCase

from calc.forms import INVALID_INPUT_ERROR, CalcInjForm, CRISimpleForm


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
