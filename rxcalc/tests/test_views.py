from django.test import TestCase


class HomePageTest(TestCase):

    def test_home_page_renders_home_page_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'rxcalc/home.html')

    def test_home_page_displays_rx(self):
        pass

    def test_home_page_uses_form(self):
        pass
