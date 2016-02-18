from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError

from common.models import Injection
from common.models import CRI


class InjectionModelTest(TestCase):

    def test_medication_string_rep(self):
        med = Injection.objects.create(name='Tramadol')
        self.assertEqual(str(med), 'Tramadol')

    def test_name_field(self):
        Injection.objects.create(name='Tramadol')
        med = Injection.objects.get(name='Tramadol')
        self.assertEqual(med, Injection.objects.first())

    def test_name_field_is_unique(self):
        med = Injection.objects.create(name='Tramadol')

        with self.assertRaises(IntegrityError):
            med_dupe = Injection.objects.create(name='Tramadol')
            med_dupe.full_clean()

    def test_concentration_field_can_be_null(self):
        med = Injection.objects.create(name='Tramadol')
        med.full_clean()
        # Should not raise

    def test_category_field(self):
        Injection.objects.create(name='Tramadol', category='pain')
        med = Injection.objects.get(category='pain')
        self.assertEqual(med, Injection.objects.first())

    def test_description_field(self):
        med = Injection.objects.create(name='Tramadol', desc='an opioid pain medication used to \
                                                        treat moderate to moderately severe pain')
        target_med = Injection.objects.get(desc='an opioid pain medication used to \
                                                        treat moderate to moderately severe pain')
        self.assertEqual(med, target_med)

    def test_factor_field_is_float(self):
        Injection.objects.create(name='Tramadol', factor=1/50)
        med = Injection.objects.first()
        self.assertAlmostEqual(med.factor * 9.2, 0.184)

    def test_medications_are_ordered_by_category(self):
        med1 = Injection.objects.create(name='Tramadol', category='pain')
        med2 = Injection.objects.create(name='Ketoprofen', category='pain')
        med3 = Injection.objects.create(name='Ampicillin', category='antibiotic')
        self.assertEqual(med3, Injection.objects.first())

    def test_slug_field_created_from_name_field(self):
        med = Injection.objects.create(name='Tramadol Super (Nighttime)')
        self.assertEqual('tramadol-super-nighttime', med.slug)


class CRITest(TestCase):

    def test_cri_model_serializes_json(self):
        dose_rates = [0.5, 0.05, 0.10, 0.010]
        med = CRI.objects.create(name='Morphine', calc_type='ez', units='mg', rates=[0.5, 0.05, 0.10, 0.010])
        self.assertEqual(dose_rates, med.rates)

    def test_cri_model_calc_type_only_has_two_choices(self):
        med = CRI.objects.create(name='Dobutamine', calc_type='adv', units='mg')
        med2 = CRI.objects.create(name='Metoclopramide', calc_type='adv', units='mg')
        med_fail = CRI(name='Drugahol', calc_type='hxc', units='kg')

        with self.assertRaises(ValidationError):
            med_fail.save()
            med_fail.full_clean()
