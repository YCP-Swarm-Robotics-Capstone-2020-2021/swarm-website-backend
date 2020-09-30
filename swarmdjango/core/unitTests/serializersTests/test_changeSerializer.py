from core.serializers import serializers
from core.models import Change, User
from django.test import TestCase
import datetime


class ChangeSerializerTest(TestCase):

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

        self.changeAttribs = {
            'user': self.user,
            'dateTime': datetime.datetime.now(),
            'context': 'Nonexistent',
            'textAdded': 'No text added',
        }

        self.change = Change.objects.create(**self.changeAttribs)
        self.serializer = serializers.ChangeSerializer(instance=self.change)
        self.data = self.serializer.data

    def testContainsExpectedFields(self):
        self.assertEqual(set(self.data.keys()), set(self.changeAttribs.keys()))