from core.serializers import serializers
from core.models import User
from django.test import TestCase


class UserSerializerTest(TestCase):
    def setUp(self):
        self.userAttribs = {
            'id': 2,
            'username': 'test6',
            'firstName': 'Test',
            'lastName': 'Testineer',
            'email': 'test@gmail.com',
            'accountLevel': 9,
            'password': 'password1',
        }
        self.user = User.objects.create(**self.userAttribs)
        self.serializer = serializers.UserSerializer(instance=self.user)
        self.data = self.serializer.data

    def testContainsExpectedFields(self):
        self.assertEqual(set(self.data.keys()), set(self.userAttribs.keys()))