from django.test import TestCase
from django.contrib.auth import get_user_model

import datetime
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

    def test_tx_sheet_saves_date_on_creation(self):
        date = datetime.date.today()
        sheet = TxSheet.objects.create(owner=self.owner, name='Poochy', comment='Euthanasia')
        self.assertEqual(date, sheet.date)


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

    def test_get_absolute_url(self):
        item = TxItem.objects.create(sheet=self.sheet, med=self.drug, dose=11, unit='mL', freq='BID')
        self.assertEqual(item.get_absolute_url(), '/tx_sheet/{}/'.format(self.sheet.id))

    def test_output_instructions(self):
        item = TxItem.objects.create(sheet=self.sheet, med=self.drug, dose=11, unit='mL', freq='BID')
        instruction = 'Take 11 mLs of Drug twice a day.'
        self.assertEqual(instruction, item.instruction)
