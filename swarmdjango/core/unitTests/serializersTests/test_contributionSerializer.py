from core.serializers import serializers
from core.models import Contribution
from django.test import TestCase


class ContributionSerializerTest(TestCase):

    def setUp(self):
        self.contributionAttribs = {
            'id': 0,
            'link': 'link to wiki page',
            'description': 'short description',
            'fileName': 'filename',
        }

        self.contribution = Contribution.objects.create(**self.contributionAttribs)
        self.serializer = serializers.ContributionSerializer(instance=self.contribution)
        self.data = self.serializer.data

    def testContainsExpectedFields(self):
        self.assertEqual(set(self.data.keys()), set(self.contributionAttribs.keys()))