from django.test import TestCase
from django.contrib.auth import get_user_model

from treatment_sheets.models import TxSheet, TxItem
from common.models import Prescription

User = get_user_model()


class TxSheetTest(TestCase):

    def test_get_absolute_url(self):
        sheet = TxSheet.objects.create()
        self.assertEqual(sheet.get_absolute_url(), '/tx_sheet/{}'.format(sheet.id))

    def test_tx_sheet_saves_owner(self):
        # Should not raise
        TxSheet(owner=User())

    def test_create_new_tx_sheet_saves_first_item(self):
        item = TxItem.objects.create()
        sheet = TxSheet.create_new(owner=User(), item=item)
        self.assertIn(item.tx_sheet, sheet)

    def test_tx_sheet_desc_is_name_and_comment(self):
        sheet = TxSheet.objects.create(name='Poochy', comment='Euthanasia')
        self.assertEqual(sheet.description, 'Poochy: Euthanasia')


class TxItemTest(TestCase):

    def test_item_related_to_tx_sheet(self):
        sheet = TxSheet.objects.create()
        item = TxItem()
        item.sheet = sheet
        item.save()
        self.assertIn(item, sheet.item_set.all())

    def test_output_instructions(self):
        item = TxItem()
        item.med = Prescription.objects.create(name='Drug')
        item.dose = 11
        item.freq = 'MLBID'
        item.save()
        instruction = 'Take 11 mL of Drug twice daily.'
        self.assertEqual(instruction, item.instruction)
