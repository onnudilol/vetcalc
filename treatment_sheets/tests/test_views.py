from django.test import TestCase
from django.contrib.auth import get_user_model

from treatment_sheets.models import TxSheet, TxItem
from treatment_sheets.forms import TxSheetForm, TxItemForm
from common.models import Prescription

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
        return self.client.post('/tx_sheet/new', data={'name': 'Nate',
                                                        'comment': 'Dogg',
                                                        'med': 1,
                                                        'dose': 3,
                                                        'freq': 'SID',
                                                        'unit': 'T'})

    def test_new_tx_sheet_view_uses_tx_sheet_template(self):
        response = self.client.get('/tx_sheet/new')
        self.assertTemplateUsed(response, 'tx_sheet/tx_sheet_new.html')

    def test_new_tx_sheet_view_uses_new_tx_sheet_forms(self):
        response = self.client.get('/tx_sheet/new')
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

        response = self.client.post('/tx_sheet/new',
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

    def test_cannot_view_other_users_list(self):
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

    def test_sheet_does_not_exist_returns_404(self):
        response = self.client.get('/tx_sheet/11/')
        self.assertEqual(404, response.status_code)


class DelItemTxSheetTest(TestCase):

    def setUp(self):
        self.owner = User.objects.create_user('Marfalo', 'marfalo@gmail.com', 'terriblepw')
        self.client.force_login(self.owner)
        self.med = Prescription.objects.create(name='meth')
        self.sheet = TxSheet.objects.create(owner=self.owner)
        self.item = TxItem.objects.create(med=self.med, sheet=self.sheet)

    def post_del(self):
        return self.client.post('/tx_sheet/1/1/del', data={'sheet_id': 1, 'item_id': 1})

    def test_del_item_does_not_del_tx_sheet(self):
        # Should not raise
        self.post_del()
        TxSheet.objects.get(id=1)

    def test_del_item_existing_tx_sheet(self):
        self.post_del()
        self.assertNotIn(self.item, self.sheet.txitem_set.all())

    def test_del_item_existing_tx_sheet_does_not_del_med(self):
        self.post_del()
        med = Prescription.objects.all()
        self.assertEqual(1, len(med))

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
        self.assertEqual(403, response.status_code)


class DelTxSheet(TestCase):

    def setUp(self):
        self.owner = User.objects.create_user('Marfalo', 'marfalo@gmail.com', 'terriblepw')
        self.client.force_login(self.owner)
        self.med = Prescription.objects.create(name='meth')
        self.sheet = TxSheet.objects.create(owner=self.owner)
        self.item = TxItem.objects.create(med=self.med, sheet=self.sheet)

    def post_del(self):
        return self.client.post('/tx_sheet/1/del', data={'sheet_id': 1})

    def test_del_tx_sheet(self):
        self.post_del()
        tx_sheet = TxSheet.objects.all()
        self.assertEqual(0, len(tx_sheet))

    def test_del_tx_sheet_also_del_related_item(self):
        self.post_del()
        item = TxItem.objects.all()
        self.assertEqual(0, len(item))

    def test_del_tx_sheet_does_not_del_med(self):
        self.post_del()
        med = Prescription.objects.all()
        self.assertEqual(1, len(med))

    def test_POST_redirects_to_tx_sheet_home_page(self):
        response = self.post_del()
        self.assertRedirects(response, '/tx_sheet/')

    def test_del_tx_sheet_login_required(self):
        self.client.logout()
        response = self.post_del()
        self.assertEqual(302, response.status_code)

    def test_cannot_del_other_users_tx_sheet(self):
        self.client.logout()
        owner2 = User.objects.create_user('Partario', 'partario@gmail.com', 'awfulpw')
        self.client.force_login(owner2)
        response = self.post_del()
        self.assertEqual(403, response.status_code)


class EditTxSheetInfoTest(TestCase):

    def setUp(self):
        self.owner = User.objects.create_user('Marfalo', 'marfalo@gmail.com', 'terriblepw')
        self.client.force_login(self.owner)
        self.med = Prescription.objects.create(name='meth')
        self.sheet = TxSheet.objects.create(owner=self.owner, name='Doge', comment='Coin')
        self.item = TxItem.objects.create(med=self.med, sheet=self.sheet)

    def test_edit_tx_sheet_view_uses_tx_sheet_form(self):
        response = self.client.get('/tx_sheet/1/edit')
        self.assertIsInstance(response.context['form'], TxSheetForm)

    def test_edit_tx_sheet_saves_changes(self):
        self.client.post('/tx_sheet/1/edit', data={'name': 'Frog', 'comment': 'Dollar'})
        sheet = TxSheet.objects.first()
        self.assertEqual('Frog', sheet.name)
        self.assertEqual('Dollar', sheet.comment)

    def test_edit_tx_sheet_redirects_to_tx_sheet(self):
        response = self.client.post('/tx_sheet/1/edit', data={'name': 'Frog', 'comment': 'Dollar'})
        self.assertRedirects(response, '/tx_sheet/1/')

    def test_cannot_edit_other_users_tx_sheet(self):
        self.client.logout()
        owner2 = User.objects.create_user('Partario', 'partario@gmail.com', 'awfulpw')
        self.client.force_login(owner2)
        response = self.client.post('/tx_sheet/1/edit', data={'name': 'Frog', 'comment': 'Dollar'})
        self.assertEqual(403, response.status_code)

    def test_edit_tx_sheet_login_required(self):
        self.client.logout()
        response = self.client.post('/tx_sheet/1/edit', data={'name': 'Frog', 'comment': 'Dollar'})
        self.assertEqual(302, response.status_code)


class OutputTxSheetPDFTest(TestCase):

    def setUp(self):
        self.owner = User.objects.create_user('Marfalo', 'marfalo@gmail.com', 'terriblepw')
        self.client.force_login(self.owner)
        self.med = Prescription.objects.create(name='meth')
        self.sheet = TxSheet.objects.create(owner=self.owner, name='Doge', comment='Coin')
        self.item = TxItem.objects.create(med=self.med, sheet=self.sheet)

    def test_output_pdf_view_login_required(self):
        self.client.logout()
        response = self.client.get('/tx_sheet/1/pdf')
        self.assertEqual(302, response.status_code)

    def test_cannot_output_pdf_other_users(self):
        self.client.logout()
        owner2 = User.objects.create_user('Partario', 'partario@gmail.com', 'awfulpw')
        self.client.force_login(owner2)
        response = self.client.get('/tx_sheet/1/pdf')
        self.assertEqual(403, response.status_code)
