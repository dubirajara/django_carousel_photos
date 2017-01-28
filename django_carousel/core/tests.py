from django.test import TestCase
from django.shortcuts import resolve_url as r
from model_mommy import mommy

from django_carousel.core.models import Photo


class HomeTest(TestCase):
    def setUp(self):
        self.photo = mommy.make('Photo')
        self.response = self.client.get(r('photo_carousel'))

    def test_get(self):
        """GET 'photo_carousel' must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """'photo_carousel' must use template photos.html"""
        self.assertTemplateUsed(self.response, 'photos.html')

    def test_admin_link(self):
        """home contains admin link"""
        expected = 'href="{}"'.format('/admin')
        self.assertContains(self.response, expected)

    def test_carousel_photo(self):
        """home contains carousel bootstrap"""
        expected = 'id="{}"'.format('carousel-example-generic')
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


class ModelTest(TestCase):
    def setUp(self):
        self.photo = mommy.make('Photo')

    def test_create(self):
        """Check models data create"""
        self.assertTrue(Photo.objects.exists())

    def test_title_can_be_blank(self):
        """Check title fields can be blank"""
        field = Photo._meta.get_field('title')
        self.assertTrue(field.blank)

    def test_description_can_be_blank(self):
        """Check description fields can be blank"""
        field = Photo._meta.get_field('description')
        self.assertTrue(field.blank)

    def test_ordering(self):
        """Check ordering to show"""
        self.assertListEqual(['timestamp'], Photo._meta.ordering)

    def test_str(self):
        """Check __str__ return title field"""
        self.assertEqual(self.photo.title, str(self.photo))
