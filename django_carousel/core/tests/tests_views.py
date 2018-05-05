from django.test import TestCase
from django.shortcuts import resolve_url as r

from model_mommy import mommy


class HomeTest(TestCase):
    def setUp(self):
        self.photo = mommy.make('Photo')
        self.response = self.client.get(r('photo_carousel'))

    def test_get(self):
        """GET 'photo_carousel' must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """'photo_carousel' must use template bootstrap.html"""
        self.assertTemplateUsed(self.response, 'bootstrap.html')

    def test_admin_link(self):
        """home contains admin link"""
        expected = 'href="{}"'.format('/admin')
        self.assertContains(self.response, expected)

    def test_carousel_photo(self):
        """home contains carousel bootstrap"""
        expected = 'id="{}"'.format('demo-carousel')
        self.assertContains(self.response, expected)

    def test_html(self):
        contents = (
            self.photo.title,
            self.photo.description,
            self.photo.image
        )
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)
