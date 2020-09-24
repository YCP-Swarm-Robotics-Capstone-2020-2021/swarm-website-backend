from core.serializers import serializers
from core.models import User
from django.test import TestCase


class UserSerializerTest(TestCase):
    def setUp(self):
        self.userAttribs = {
                    'email': 'test@gmail.com',
                    'lastName': 'Testineer',
                    'firstName': 'Test',
                    'password': 'password1',
                    'username': 'test6',

        }
        self.user = User.objects.create(**self.userAttribs)
        self.serializer = serializers.UserSerializer(instance=self.user)
        self.data = self.serializer.data

    def testContainsExpectedFields(self):
        self.assertEqual(set(self.data.keys()), self.userAttribs.keys())