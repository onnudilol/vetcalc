from django.test import TestCase
from django.contrib.auth import get_user_model
from django.http import HttpRequest

from treatment_sheets.models import TxSheet, TxItem
from treatment_sheets.forms import TxSheetForm, TxItemForm
from treatment_sheets.views import view_treatment_sheet, new_tx_sheet
from common.models import Prescription

from unittest.mock import patch, Mock

User = get_user_model()


class TxSheetPageTest(TestCase):

    def test_tx_sheet_view_uses_tx_sheet_template(self):
        response = self.client.get('/tx_sheet/')
        self.assertTemplateUsed(response, 'tx_sheet/tx_sheet.html')

    def test_tx_sheet_view_only_retrieves_owners_list(self):
        owner = User.objects.create(username='Marfalo')
        sheet = TxSheet.objects.create(owner=owner, name='snoop', comment='dogg')
        self.client.force_login(owner)

        response = self.client.get('/tx_sheet/')

        self.assertContains(response, sheet.__str__())

    def test_tx_sheet_view_does_not_display_lists_for_anonymous_users(self):
        owner = User.objects.create(username='Marfalo')
        sheet = TxSheet.objects.create(owner=owner, name='snoop', comment='dogg')

        response = self.client.get('/tx_sheet/')

        self.assertNotContains(response, sheet.__str__())


class NewTxSheetTest(TestCase):

    def setUp(self):
        Prescription.objects.create(name='meth')
        self.owner = User.objects.create_user('Marfalo', 'marfalo@gmail.com', 'terriblepw')
        self.client.force_login(self.owner)

    def post_list(self):
        return self.client.post('/tx_sheet/new/', data={'name': 'Nate',
                                                        'comment': 'Dogg',
                                                        'med': 1,
                                                        'dose': 3,
                                                        'freq': 'SID',
                                                        'unit': 'T'})

    def test_new_tx_sheet_view_uses_tx_sheet_template(self):
        response = self.client.get('/tx_sheet/new/')
        self.assertTemplateUsed(response, 'tx_sheet/tx_sheet_new.html')

    def test_new_tx_sheet_view_uses_new_tx_sheet_forms(self):
        response = self.client.get('/tx_sheet/new/')
        self.assertIsInstance(response.context['sheet_form'], TxSheetForm)
        self.assertIsInstance(response.context['item_form'], TxItemForm)

    def test_create_new_tx_sheet(self):
        # Should not raise
        self.post_list()
        TxSheet.objects.first()

    def test_new_tx_sheet_login_required(self):
        self.client.logout()
        response = self.post_list()
        self.assertEqual(302, response.status_code)

    def test_new_tx_sheet_saves_owner(self):
        self.post_list()
        sheet = TxSheet.objects.first()
        self.assertEqual(self.owner, sheet.owner)

    def test_POST_redirects_to_tx_sheet_page(self):
        response = self.post_list()
        self.assertRedirects(response, '/tx_sheet/1/')

    def test_view_rejects_invalid_input(self):

        response = self.client.post('/tx_sheet/new/',
                                    data={'name': 0o010100000110111101101111011000110110100001111001,
                                          'comment': 'h',
                                          'med': 1,
                                          'dose': 3,
                                          'freq': 'TBID',
                                          'unit': 'C'})

        self.assertNotEqual(response.status_code, 302)


class ViewTxSheetTest(TestCase):

    def setUp(self):
        self.owner = User.objects.create_user('Marfalo', 'marfalo@gmail.com', 'terriblepw')
        self.client.force_login(self.owner)
        self.med = Prescription.objects.create(name='meth')
        self.sheet = TxSheet.objects.create(owner=self.owner)
        self.item = TxItem.objects.create(sheet=self.sheet, med=self.med)

    def test_edit_tx_sheet_view_uses_view_tx_sheet_template(self):
        response = self.client.get('/tx_sheet/1/')
        self.assertTemplateUsed(response, 'tx_sheet/tx_sheet_view.html')

    def test_view_tx_sheet_login_required(self):
        self.client.logout()
        response = self.client.get('/tx_sheet/1/')
        self.assertEqual(302, response.status_code)

    def test_view_retrieves_correct_list(self):
        wrong_list = TxSheet.objects.create(owner=self.owner)
        response = self.client.get('/tx_sheet/1/')
        self.assertNotEqual(wrong_list, response.context['sheet'])

    def cannot_view_other_users_list(self):
        self.client.logout()
        owner2 = User.objects.create_user('Partario', 'partario@gmail.com', 'awfulpw')
        self.client.force_login(owner2)

        response = self.client.get('/tx_sheet/1/')

        self.assertEqual(403, response.status_code)
        self.client.logout()

    def test_list_only_displays_related_items(self):
        wrong_sheet = TxSheet.objects.create(owner=self.owner)
        wrong_drug = TxItem.objects.create(sheet=wrong_sheet, med=self.med)
        response = self.client.get('/tx_sheet/1/')
        self.assertNotIn(wrong_drug, response.context['sheet'].txitem_set.all())

    def test_tx_sheet_view_uses_tx_item_form(self):
        response = self.client.get('/tx_sheet/1/')
        self.assertIsInstance(response.context['form'], TxItemForm)

    def test_add_item_existing_tx_sheet(self):
        self.client.post('/tx_sheet/1/', data={'med': 1,
                                               'dose': 11,
                                               'freq': 'BID',
                                               'unit': 'T'})
        new_item = TxItem.objects.get(id=2)
        self.assertIn(new_item, self.sheet.txitem_set.all())

    def test_POST_redirects_to_tx_sheet_page(self):
        response = self.client.post('/tx_sheet/1/', data={'med': 1,
                                                          'dose': 11,
                                                          'freq': 'BID',
                                                          'unit': 'T'})
        self.assertRedirects(response, '/tx_sheet/1/')


class DelItemTxSheetTest(TestCase):

    def setUp(self):
        self.owner = User.objects.create_user('Marfalo', 'marfalo@gmail.com', 'terriblepw')
        self.client.force_login(self.owner)
        self.med = Prescription.objects.create(name='meth')
        self.sheet = TxSheet.objects.create(owner=self.owner)
        self.item = TxItem.objects.create(med=self.med, sheet=self.sheet)

    def post_del(self):
        return self.client.post('/tx_sheet/1/del/1', data={'sheet_id': 1, 'item_id': 1})

    def test_del_item_existing_tx_sheet(self):
        self.post_del()
        TxSheet.objects.get(id=1)
        self.assertNotIn(self.item, self.sheet.txitem_set.all())

    def test_POST_redirects_to_tx_sheet_page(self):
        response = self.post_del()
        self.assertRedirects(response, '/tx_sheet/1/')

    def test_del_item_requires_login(self):
        self.client.logout()
        response = self.post_del()
        self.assertEqual(302, response.status_code)

    def test_cannot_del_other_users_tx_sheet_items(self):
        self.client.logout()
        owner2 = User.objects.create_user('Partario', 'partario@gmail.com', 'awfulpw')
        self.client.force_login(owner2)

        response = self.post_del()
        self.assertEqual(302, response.status_code)
        self.client.logout()
