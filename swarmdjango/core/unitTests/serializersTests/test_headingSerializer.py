from core.serializers import serializers
from core.models import Heading
from django.test import TestCase

class HeadingSerializerTest(TestCase):
    def setUp(self):
        self.headingAttribs = {
            'title': 'Test Title',
            'text': 'Test body test'
            # No many to many fields
        }

        self.heading = Heading.objects.create(**self.headingAttribs)
        self.serializer = serializers.HeadingSerializer(instance=self.heading)
        self.data = self.serializer.data

    def testContainsExpectedFields(self):
        for key in self.headingAttribs.keys():
            self.assertIn(key, self.data.keys())