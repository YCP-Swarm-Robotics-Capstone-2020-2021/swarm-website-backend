from core.serializers import serializers
from core.models import Log
from django.test import TestCase
from django.utils import timezone

class LogSerializerTest(TestCase):
    def setUp(self):
        date = timezone.now()
        self.logAttribs = {
            'id': 0,
            'dateTime': date,
            'deviceID': 'Dolphin0',
            'filePath': 'test/file/path',
            'log': {
                'test': 'test text',
            }
        }
        self.log = Log.objects.create(**self.logAttribs)
        self.serializer = serializers.LogSerializer(instance=self.log)
        self.data = self.serializer.data

    def testContainsExpectedFields(self):
        self.assertEqual(set(self.data.keys()), set(self.logAttribs))