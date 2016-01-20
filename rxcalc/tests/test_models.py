from django.test import TestCase
from django.db import IntegrityError

from rxcalc.models import Medication


class MedicationModelTest(TestCase):

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

    def test_description_field(self):
        med = Medication.objects.create(name='Tramadol', desc='an opioid pain medication used to \
                                                        treat moderate to moderately severe pain')
        target_med = Medication.objects.get(desc='an opioid pain medication used to \
                                                        treat moderate to moderately severe pain')
        self.assertEqual(med, target_med)

    def test_medication_string_rep(self):
        med = Medication.objects.create(name='Tramadol')
        self.assertEqual(str(med), 'Tramadol')

