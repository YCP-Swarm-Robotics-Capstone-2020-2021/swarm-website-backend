from core.serializers import serializers
from core.models import SponsorPersonalPage
from django.test import TestCase


class SponsorPersonalPageTest(TestCase):
    def setUp(self):
        self.pageAttribs = {
            'id': 0,
            'pageType': 'Sponsor page',
            'pageTitle': 'Test Sponsor Page',
            'missionStatement': 'Test statement',
            'reasonForSponsorship': 'Test reason for sponsor',
            'companyLink': 'https://company.com'
        }

        self.page = SponsorPersonalPage.objects.create(**self.pageAttribs)
        self.serializer = serializers.SponsorPersonalPageSerializer(instance=self.page)
        self.data = self.serializer.data

    def testContainsExpectedFields(self):
        self.assertEqual(set(self.data.keys()), set(self.pageAttribs.keys()))