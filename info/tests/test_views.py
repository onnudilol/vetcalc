from django.test import TestCase


class InfoTest(TestCase):

    def test_info_page_renders_info_page_template(self):
        response = self.client.get('/calc/info/')
        self.assertTemplateUsed(response, 'info/info.html')

    def test_info_page_displays_all_medications(self):
        tram = Injection.objects.create(name='Tramadol')
        ampi = Injection.objects.create(name='Ampicillin')
        response = self.client.get('/calc/info/')
        self.assertIn(tram, response.context['inj'])
        self.assertIn(ampi, response.context['inj'])


class InfoInjTest(TestCase):

    def test_rx_page_url_corresponds_to_rx_slug(self):
        inj = Injection.objects.create(name='Super Tramadol (Nighttime)')
        response = self.client.get('/calc/info/{}/'.format(inj.slug))
        self.assertEqual(200, response.status_code)

    def test_rx_info_renders_rx_info_template(self):
        Injection.objects.create(name='Super Tramadol Nighttime')
        response = self.client.get('/calc/info/super-tramadol-nighttime/')
        self.assertTemplateUsed(response, 'calc/rx.html')
