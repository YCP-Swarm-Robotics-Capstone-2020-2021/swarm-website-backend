from core.serializers import serializers
from core.models import Run, Log
from django.test import TestCase
from django.utils import timezone

class RunSerializerTest(TestCase):
    def setUp(self):
        date = timezone.now()
        self.logAttribs = {
            'dateTime': date,
            'deviceID': 'Dolphin0',
            'filePath': 'test/file/path',
            'log': {
                'test': 'test text',
            }
        }
        self.log = Log.objects.create(**self.logAttribs)
        self.runAttribs = {
            'dateTime': date,
            'deviceID': 'Dolphin0',
            'logID': self.log,
            'runID': 10,
            'run': {10: 'run'}
        }

        self.run = Run.objects.create(**self.runAttribs)
        self.serializer = serializers.RunSerializer(instance=self.run)
        self.data = self.serializer.data

    def testContainsExpectedFields(self):
        for key in self.runAttribs:
            self.assertIn(key, self.data.keys())
