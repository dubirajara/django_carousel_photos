from datetime import datetime
from shutil import rmtree

from django.conf import settings
from django.test import TestCase

from model_mommy import mommy

from django_carousel.core.models import Photo


class ModelTest(TestCase):
    def setUp(self):
        self.photo = mommy.make('Photo')

    def test_create(self):
        """Check models data create"""
        self.assertTrue(Photo.objects.exists())

    def tearDown(self):
        rmtree(settings.MEDIA_ROOT, ignore_errors=True)

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

    def test_timestamp(self):
        """photo must have an auto timestamp attr."""
        self.assertIsInstance(self.photo.timestamp, datetime)

    def test_str(self):
        """Check __str__ return title field"""
        self.assertEqual(self.photo.title, str(self.photo))
