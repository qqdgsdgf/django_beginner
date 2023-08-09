# pages/tests.py
from django.test import SimpleTestCase
from django.urls import reverse


class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/pages/') # put url here
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('home')) # use name defined in urls.py
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  # new
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, '../templates/pages/home.html')

    def test_template_content(self):  # new
        response = self.client.get(reverse('home'))
        self.assertContains(response, '<h1>Homepage</h1>')

class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/pages/about/')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  # new
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  # new
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, '../templates/pages/about.html')

    def test_template_content(self):  # new
        response = self.client.get(reverse('about'))
        self.assertContains(response, '<h1>About page</h1>')
