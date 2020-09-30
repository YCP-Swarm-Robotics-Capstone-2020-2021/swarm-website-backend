from core.serializers import serializers
from core.models import Comment, User
from django.test import TestCase
import datetime


class CommentSerializerTest(TestCase):

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

        self.commentAttribs = {
            'user': self.user,
            'dateTime': datetime.datetime.now(),
            'text': 'No text added',

            # Did not do replies because Many to many field

        }

        self.comment = Comment.objects.create(**self.commentAttribs)

        self.serializer = serializers.CommentSerializer(instance=self.comment)
        self.data = self.serializer.data

    def testContainsExpectedFields(self):
        for key in self.commentAttribs.keys():
            self.assertIn(key, self.data.keys())
