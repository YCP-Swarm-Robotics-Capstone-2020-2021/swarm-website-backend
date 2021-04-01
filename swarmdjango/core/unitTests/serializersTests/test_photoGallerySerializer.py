from core.serializers import serializers
from core.models import PhotoGallery, User
from django.test import TestCase
import datetime


class PhotoGallerySerializerTest(TestCase):
    def setUp(self):
        self.userAttribs = {
            'email': 'test@gmail.com',
            'lastName': 'Testineer',
            'firstName': 'Test',
            'password': 'password1',
            'username': 'test6',
            'id': '1',
        }
        self.user = User.objects.create(**self.userAttribs)

        self.photoGalleryAttribs = {
            'id': 0,
            'fileName': 'Test/File/name',
            'caption': 'Test caption',
            'uploadedBy': self.user
        }

        self.photoGallery = PhotoGallery.objects.create(**self.photoGalleryAttribs)
        self.serializer = serializers.PhotoGallerySerializer(instance=self.photoGallery)
        self.data = self.serializer.data

    def testContainsExpectedFields(self):
        self.assertEqual(set(self.data.keys()), set(self.photoGalleryAttribs.keys()))