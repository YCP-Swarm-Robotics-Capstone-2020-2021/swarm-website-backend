from core.serializers import serializers
from core.models import Developer, PersonalPage
from django.test import TestCase


class DeveloperSerializerTest(TestCase):

    def setUp(self):
        self.personalPageAttribs = {
            'pageType': 'dev page',
            'pageTitle': 'Test Dev Page'
        }
        self.personalPage = PersonalPage.objects.create(**self.personalPageAttribs)

        self.developerAttribs = {
            'teamRole': 'software engineer',
            'page': self.personalPage,
        }

        self.developer = Developer.objects.create(**self.developerAttribs)
        self.serializer = serializers.DeveloperSerializer(instance=self.developer)
        self.data = self.serializer.data

    def testContainsExpectedFields(self):
        self.assertEqual(set(self.data.keys()), set(self.developerAttribs.keys()))