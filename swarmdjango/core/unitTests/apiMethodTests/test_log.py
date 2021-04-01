from rest_framework.test import APIRequestFactory
from core.serializers import serializers
from django.test import TestCase
from core.models import Log
from django.utils import timezone

class LogTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
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
        self.log.save()

    def testGetLog(self):
        request = self.factory.get('/api/log/0')