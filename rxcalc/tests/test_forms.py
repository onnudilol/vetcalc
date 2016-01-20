from django.test import TestCase

from rxcalc.forms import INVALID_INPUT_ERROR, WeightForm


class WeightFormTest(TestCase):

    def test_form_accepts_integer_input(self):
        pass

    def test_form_accepts_float_input(self):
        pass

    def test_form_rejects_non_numeric_input(self):
        form = WeightForm(data={'weight': 'a string'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['weight'], [INVALID_INPUT_ERROR])
