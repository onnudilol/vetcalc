from django.test import TestCase
from django.contrib.auth import get_user_model

from unittest.mock import patch, Mock

from treatment_sheets.forms import NewTxSheetForm, EditTxSheetForm

User = get_user_model()


class NewTxSheetFormTest(TestCase):

    def test_form_validation(self):
        drug = Mock(spec='treatment_sheets.forms.Prescription')
        form = NewTxSheetForm(data={
            'name': '',
            'comment': '',
            'med': drug,
            'dose': '',
            'freq': '',
            'unit': ''
        })
        self.assertFalse(form.is_valid())

    @patch('treatment_sheets.forms.TxSheet.create_new')
    def test_form_save(self, mock_create_new):
        owner = Mock(is_authenticated=lambda: True)
        drug = Mock(spec='treatment_sheets.forms.Prescription')
        drug.name = 'Morphine'
        sheet = mock_create_new.return_value

        form = NewTxSheetForm(data={
            'name': 'Poochy',
            'comment': 'Neuter',
            'med': drug,
            'dose': '5',
            'freq': 'BID',
            'unit': 'T'
        })

        sheet2 = form.save(owner=owner)
        self.assertEqual(sheet, sheet2)


class EditTxSheetFormTest(TestCase):

    def test_form_validation(self):
        drug = Mock(spec='treatment_sheets.forms.Prescription')
        form = EditTxSheetForm(data={
            'med': drug,
            'dose': '',
            'freq': '',
            'unit': ''
        })
        self.assertFalse(form.is_valid())
