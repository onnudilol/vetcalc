from django.test import TestCase
from django.db import IntegrityError

from rxcalc.models import Medication


class MedicationModelTest(TestCase):

    def test_medication_string_rep(self):
        med = Medication.objects.create(name='Tramadol')
        self.assertEqual(str(med), 'Tramadol')

    def test_name_field(self):
        Medication.objects.create(name='Tramadol')
        med = Medication.objects.get(name='Tramadol')
        self.assertEqual(med, Medication.objects.first())

    def test_name_field_is_unique(self):
        med = Medication.objects.create(name='Tramadol')

        with self.assertRaises(IntegrityError):
            med_dupe = Medication.objects.create(name='Tramadol')
            med_dupe.full_clean()

    def test_concentration_field_can_be_null(self):
        med = Medication.objects.create(name='Tramadol')
        med.full_clean()
        # Should not raise

    def test_category_field(self):
        Medication.objects.create(name='Tramadol', category='pain')
        med = Medication.objects.get(category='pain')
        self.assertEqual(med, Medication.objects.first())

    def test_description_field(self):
        med = Medication.objects.create(name='Tramadol', desc='an opioid pain medication used to \
                                                        treat moderate to moderately severe pain')
        target_med = Medication.objects.get(desc='an opioid pain medication used to \
                                                        treat moderate to moderately severe pain')
        self.assertEqual(med, target_med)

    def test_factor_field_is_float(self):
        Medication.objects.create(name='Tramadol', factor=1/50)
        med = Medication.objects.first()
        self.assertAlmostEqual(med.factor * 9.2, 0.184)

    def test_medications_are_ordered_by_category(self):
        med1 = Medication.objects.create(name='Tramadol', category='pain')
        med2 = Medication.objects.create(name='Ketoprofen', category='pain')
        med3 = Medication.objects.create(name='Ampicillin', category='antibiotic')
        self.assertEqual(med3, Medication.objects.first())

    def test_slug_field_created_from_name_field(self):
        med = Medication.objects.create(name='Tramadol Super (Nighttime)')
        self.assertEqual('tramadol-super-nighttime', med.slug)

    def test_get_absolute_url(self):
        pass
