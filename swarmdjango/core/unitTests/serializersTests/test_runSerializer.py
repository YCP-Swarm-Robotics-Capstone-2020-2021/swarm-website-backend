from core.serializers import serializers
from core.models import Run
from django.test import TestCase
from django.utils import timezone

class RunSerializerTest(TestCase):
    def setUp(self):
        date = timezone.now()
        self.runAttribs = {
            'dateTime': date
            # Skip many to many
        }
        self.run = Run.objects.create(**self.runAttribs)
        self.serializer = serializers.RunSerializer(instance=self.run)
        self.data = self.serializer.data

    def testContainsExpectedFields(self):
        for key in self.runAttribs:
            self.assertIn(key, self.data.keys())
