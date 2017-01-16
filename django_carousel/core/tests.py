from django.test import TestCase
from django.shortcuts import resolve_url as r


class HomeTest(TestCase):

    def setUp(self):
        self.response = self.client.get(r('photo_carousel'))

    def test_get(self):
        """GET 'photo_carousel' must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """'photo_carousel' must use template photos.html"""
        self.assertTemplateUsed(self.response, 'photos.html')
