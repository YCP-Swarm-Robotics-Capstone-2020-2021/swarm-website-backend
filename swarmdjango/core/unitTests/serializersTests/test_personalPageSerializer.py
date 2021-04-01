from core.serializers import serializers
from core.models import PersonalPage
from django.test import TestCase


class PersonalPageSerializerTest(TestCase):
    def setUp(self):
        self.personalPageAttribs = {
            'id': 0,
            'pageType': 'Sponsor page',
            'pageTitle': 'Test Sponsor Page'
        }

        self.personalPage = PersonalPage.objects.create(**self.personalPageAttribs)
        self.serializer = serializers.PersonalPageSerializer(instance=self.personalPage)
        self.data = self.serializer.data

    def testContainsExpectedFields(self):
        self.assertEqual(set(self.data.keys()), set(self.personalPageAttribs.keys()))