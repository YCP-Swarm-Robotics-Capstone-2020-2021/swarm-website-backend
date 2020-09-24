from core.serializers import serializers
from core.models import Admin
from django.test import TestCase


class AdminSerializerTest(TestCase):

    def setUp(self):
        self.adminAttribs = {
            'email': 'test@gmail.com',
            'lastName': 'Testineer',
            'firstName': 'Test',
            'password': 'password1',
            'username': 'test6',
            'id': '1',
            'receiveUpdates': 'True',
        }

        self.admin = Admin.objects.create(**self.adminAttribs)
        self.serializer = serializers.AdminSerializer(instance=self.admin)
        self.data = self.serializer.data

    def testContainsExpectedFields(self):
        self.assertEqual(set(self.data.keys()), set(self.adminAttribs.keys()))