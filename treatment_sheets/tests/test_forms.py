from django.test import TestCase
from django.contrib.auth import get_user_model

from unittest.mock import Mock

from treatment_sheets.forms import TxSheetForm, TxItemForm
from treatment_sheets.models import TxSheet, TxItem, Prescription

User = get_user_model()


class TxSheetFormTest(TestCase):

    def test_form_validation(self):
        drug = Mock(spec='treatment_sheets.forms.Prescription')
        form = TxSheetForm(data={
            'name': '',
            'comment': '',
            'med': drug,
            'dose': '',
            'freq': '',
            'unit': ''
        })
        self.assertFalse(form.is_valid())

    def test_form_save_sheet(self):
        owner = User.objects.create()

        form = TxSheetForm(data={
            'name': 'Poochy',
            'comment': 'Neuter'
        })

        form.is_valid()
        sheet = form.save(owner=owner)
        self.assertIsInstance(sheet, TxSheet)


class TxItemFormTest(TestCase):

    def test_form_validation(self):
        drug = Mock(spec=Prescription)
        form = TxItemForm(data={
            'med': drug,
            'dose': '',
            'freq': '',
            'unit': ''
        })
        self.assertFalse(form.is_valid())

    def test_form_save_item(self):
        sheet = Mock(spec=TxSheet)
        sheet._state = Mock()
        sheet._state.db = None
        sheet.id = 1
        Prescription.objects.create(name='Drugahol')

        form = TxItemForm(data={
            'med': 1,
            'dose': 5,
            'freq': 'BID',
            'unit': 'T'
        })

        form.is_valid()
        sheet = form.save(sheet=sheet)
        self.assertIsInstance(sheet, TxItem)
