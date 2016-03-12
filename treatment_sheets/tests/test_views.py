from django.test import TestCase
from django.contrib.auth import get_user_model

from treatment_sheets.models import TxSheet, TxItem
from treatment_sheets.forms import NewTxSheetForm, EditTxSheetForm
from common.models import Prescription

from unittest.mock import patch

User = get_user_model()


class TxSheetPageTest(TestCase):

    def test_tx_sheet_view_uses_tx_sheet_template(self):
        response = self.client.get('/tx_sheet/')
        self.assertTemplateUsed(response, 'tx_sheet/tx_sheet_list.html')

    def test_tx_sheet_view_only_retrieves_owners_list(self):
        owner = User.objects.create(name='Marfalo')
        sheet = TxSheet.objects.create(owner=owner)
        self.client.force_login(owner)

        response = self.client.get('/tx_sheet/')

        self.assertIn(sheet, response.context)

    def test_tx_sheet_view_does_not_display_lists_for_anonymous_users(self):
        owner = User.objects.create(name='Marfalo')
        sheet = TxSheet.objects.create(owner=owner)

        response = self.client.get('/tx_sheet/')

        self.assertNotIn(sheet, response.context)


class NewTxSheetTest(TestCase):

    def setUp(self):
        Prescription.objects.create(name='meth')
        self.owner = User.objects.create_user('Marfalo', 'marfalo@gmail.com', 'terriblepw')
        self.client.force_login(self.owner)

    def post_test_list(self):
        return self.client.post('/tx_sheet/new/',
                                data={'name': 'Poochy',
                                      'rx': 1,
                                      'dose': '3',
                                      'freq': 'TBID'})

    def test_new_tx_sheet_view_uses_tx_sheet_template(self):
        response = self.client.get('/tx_sheet/new/')
        self.assertTemplateUsed(response, 'tx_sheet/new.html')

    def test_new_tx_sheet_view_uses_new_tx_sheet_form(self):
        response = self.client.get('/tx_sheet/new/')
        self.assertIn(response.context['form'], NewTxSheetForm)

    @patch('treatment_sheets.views.NewTxSheetForm')
    def test_create_new_tx_sheet(self, mock_newtxsheetform):
        tx_form = mock_newtxsheetform.save.return_value
        tx_form.is_valid.return_value = True
        new_list = tx_form.save.return_value

        response = self.post_test_list()

        self.assertIn(new_list, response.context)

    def test_new_tx_sheet_login_required(self):
        self.client.logout()
        response = self.post_test_list()
        self.assertEqual(403, response.status_code)

    @patch('treatment_sheets.views.NewTxSheetForm')
    def test_new_tx_sheet_saves_owner(self, mock_newtxsheetform):
        tx_form = mock_newtxsheetform.return_value
        tx_form.is_valid.return_value = True

        self.post_test_list()

        tx_form.saved.assert_called_with(owner=self.owner)

    @patch('treatment_sheets.views.redirect')
    @patch('treatment_sheets.views.NewTxSheetForm')
    def test_POST_redirects_to_tx_sheet_page(self, mock_newtxsheetform, mock_redirect):
        tx_form = mock_newtxsheetform.return_value
        tx_form.is_valid.return_value = True
        list_redirect = mock_redirect.return_value

        response = self.post_test_list()

        self.assertEqual(response, list_redirect)

    def test_view_rejects_invalid_input(self, mock_newtxsheetform):
        invalid_tx_sheet = mock_newtxsheetform.return_value
        invalid_tx_sheet.is_valid.return_value = False

        response = self.client.post('/tx_sheet/new/',
                                    data={'name': 0o010100000110111101101111011000110110100001111001,
                                          'rx': 'Tylenol',
                                          'dose': 3,
                                          'freq': 'TBID'})

        self.assertFalse(invalid_tx_sheet.save.called)


class ViewTxSheetTest(TestCase):

    def setUp(self):
        self.owner = User.objects.create_user('Marfalo', 'marfalo@gmail.com', 'terriblepw')
        self.client.force_login(self.owner)
        Prescription.objects.create(name='meth')
        TxItem.objects.create(rx_id=1)
        TxSheet.objects.create(owner=self.owner, item_id=1)

    def test_edit_tx_sheet_view_uses_view_tx_sheet_template(self):
        response = self.client.get('/tx_sheet/1/')
        self.assertTemplateUsed(response, 'tx_sheet/tx_sheet_view.html')

    def test_view_tx_sheet_login_required(self):
        self.client.logout()
        response = self.client.get('/tx_sheet/1/')
        self.assertEqual(403, response.status_code)

    def test_view_retrieves_correct_list(self):
        wrong_list = TxSheet.objects.create(id=2)
        response = self.client.get('/tx_sheet/1/')
        self.assertNotIn(response.context, wrong_list)

    def cannot_view_other_users_list(self):
        self.client.logout()
        owner2 = User.objects.create_user('Partario', 'partario@gmail.com', 'awfulpw')
        self.client.force_login(owner2)

        response = self.client.get('/tx_sheet/1/')

        self.assertEqual(403, response.status_code)
        self.client.logout()

    def test_list_only_displays_related_items(self):
        wrong_drug = TxItem.objects.create(name='morphine')
        response = self.client.get('/tx_sheet/1/')
        self.assertNotIn(wrong_drug, response.context)


class AddItemTxSheet(TestCase):

    def setUp(self):
        self.owner = User.objects.create_user('Marfalo', 'marfalo@gmail.com', 'terriblepw')
        self.client.force_login(self.owner)
        Prescription.objects.create(name='meth')
        TxItem.objects.create(rx_id=1)
        TxSheet.objects.create(owner=self.owner, item_id=1)

    def add_tx_item_view_uses_add_tx_item_template(self):
        response = self.client.get('/tx_sheet/1/add')
        self.assertTemplateUsed(response, 'tx_sheet/tx_sheet_add.html')

    def test_edit_tx_sheet_view_uses_edit_tx_sheet_form(self):
        response = self.client.get('/tx_sheet/1/')
        self.assertIsInstance(response.context['form'], EditTxSheetForm)

    def add_tx_item_requires_login(self):
        self.client.logout()
        response = self.client.get('/tx_sheet/1/add')
        self.assertEqual(403, response.status_code)

    @patch('treatment_sheets.views.EditTxSheetForm')
    def test_add_item_existing_tx_sheet(self, mock_edittxsheetform):
        mock_form = mock_edittxsheetform.return_value
        mock_form.is_valid.return_value = True
        mock_item = mock_form.save.return_value

        self.client.post('/tx_sheet/1/add', data={'rx': 1,
                                                  'dose': 11,
                                                  'freq': 'mlbid'})

        self.assertTrue(mock_item.called)

    @patch('treatment_sheets.views.EditTxSheetForm')
    @patch('treatment_sheets.views.redirect')
    def test_POST_redirects_to_tx_sheet_page(self, mock_redirect, mock_edittxsheetform):
        mock_form = mock_edittxsheetform.return_value
        mock_form.is_valid.return_value = True
        mock_list = mock_form.save.return_value

        self.client.post('/tx_sheet/1/add', data={'rx': 1,
                                                  'dose': 11,
                                                  'freq': 'mlbid'})

        mock_redirect.assert_called_once_with(mock_list)


class DelItemTxSheet(TestCase):

    def setUp(self):
        self.owner = User.objects.create_user('Marfalo', 'marfalo@gmail.com', 'terriblepw')
        self.client.force_login(self.owner)
        Prescription.objects.create(name='meth')
        self.item = TxItem.objects.create(rx_id=1)
        self.sheet = TxSheet.objects.create(owner=self.owner, item_id=1)

    def test_del_item_existing_tx_sheet(self):
        self.client.post('/tx_sheet/1/del', data={'item': 1})
        TxSheet.objects.get(id=1)
        self.assertNotIn(self.item, TxSheet.item_set.all())

    @patch('treatment_sheets.views.redirect')
    def test_POST_redirects_to_tx_sheet_page(self, mock_redirect):
        mock_redirect.assert_called_once_with(self.sheet.id)

    def test_del_item_requires_login(self):
        self.client.logout()
        response = self.client.post('/tx_sheet/1/del', data={'item': 1})
        self.assertEqual(403, response.status_code)

    def test_cannot_del_other_users_tx_sheet_items(self):
        self.client.logout()
        owner2 = User.objects.create_user('Partario', 'partario@gmail.com', 'awfulpw')
        self.client.force_login(owner2)

        response = self.client.post('/tx_sheet/1/del', data={'item': 1})
        self.assertEqual(403, response.status_code)
        self.client.logout()
