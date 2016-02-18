from django.test import TestCase


class HomePageTest(TestCase):

    def test_home_page_renders_home_page_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_view_sets_active_class_on_link(self):
        response = self.client.get('/')
        self.assertEqual('home', response.context['navbar'])
