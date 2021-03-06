from django.test import TestCase
from model_mommy import mommy

from aloisioimoveis.properties.models import Photo


class PhotoModelTest(TestCase):
    def setUp(self):
        self.obj = mommy.make(Photo, image='photo.jpg')

    def test_create(self):
        """Should create a Photo"""
        self.assertTrue(Photo.objects.exists())
