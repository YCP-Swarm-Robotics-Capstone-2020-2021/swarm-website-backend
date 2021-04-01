from core.serializers import serializers
from core.models import Sponsor, PersonalPage
from django.test import TestCase


class SponsorSerializerTest(TestCase):
    def setUp(self):
        self.personalPageAttribs = {
            'id': 0,
            'pageType': 'Sponsor page',
            'pageTitle': 'Test Sponsor Page'
        }
        self.personalPage = PersonalPage.objects.create(**self.personalPageAttribs)

        self.sponsorAttribs = {
            'id': 0,
            'email': 'sponsor@gmail.com',
            'firstName': 'Beckton',
            'lastName': 'Dickinson',
            'username': 'BD',
            'accountLevel': 3,
            'password': 'yeet',
            'companyName': 'Beckton D',
            'page': self.personalPage
        }
        self.sponsor = Sponsor.objects.create(**self.sponsorAttribs)
        self.serializer = serializers.SponsorSerializer(instance=self.sponsor)
        self.data = self.serializer.data

    def testContainsExpectedFields(self):
        self.assertEqual(set(self.data.keys()), set(self.sponsorAttribs.keys()))
