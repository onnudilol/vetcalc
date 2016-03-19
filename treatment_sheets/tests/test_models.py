from django.test import TestCase
from django.contrib.auth import get_user_model

from treatment_sheets.models import TxSheet, TxItem
from common.models import Prescription

User = get_user_model()


class TxSheetTest(TestCase):

    def setUp(self):
        self.owner = User.objects.create(username='Marfalo')

    def test_get_absolute_url(self):
        sheet = TxSheet.objects.create(owner=self.owner)
        self.assertEqual(sheet.get_absolute_url(), '/tx_sheet/{}/'.format(sheet.id))

    def test_tx_sheet_saves_owner(self):
        # Should not raise
        TxSheet(owner=User())

    def test_create_new_tx_sheet_saves_first_item(self):
        drug = Prescription.objects.create(name='Robitussin')
        sheet = TxSheet.create_new(owner=self.owner, med=drug, dose=5, freq='SID', unit='C')
        item = TxItem.objects.first()
        self.assertEqual(item.sheet, sheet)
        self.assertIn('Take 5 Capsules of Robitussin once a day.', item.instruction)

    def test_tx_sheet_desc_is_name_and_comment(self):
        sheet = TxSheet.objects.create(owner=self.owner, name='Poochy', comment='Euthanasia')
        self.assertEqual(sheet.description, 'Poochy: Euthanasia')


class TxItemTest(TestCase):

    def setUp(self):
        self.sheet = TxSheet.objects.create(owner=User.objects.create())
        self.drug = Prescription.objects.create(name='Drug')

    def test_item_related_to_tx_sheet(self):

        item = TxItem()
        item.med = self.drug
        item.sheet = self.sheet
        item.save()

        self.assertEqual(self.sheet.id, item.sheet_id)

    def test_output_instructions(self):
        item = TxItem.objects.create(sheet=self.sheet, med=self.drug, dose=11, unit='mL', freq='BID')
        instruction = 'Take 11 mLs of Drug twice a day.'
        self.assertEqual(instruction, item.instruction)
