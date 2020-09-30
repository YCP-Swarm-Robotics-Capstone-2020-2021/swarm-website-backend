from core.serializers import serializers
from core.models import Log, Robot, Run
from django.test import TestCase
from django.utils import timezone

import ipaddress

class LogSerializerTest(TestCase):
    def setUp(self):
        self.robotAttribs = {
            'name': 'Robot1',
            'ip': '0.0.0.0'
        }
        self.robot = Robot.objects.create(**self.robotAttribs)

        date = timezone.now()
        self.runAttribs = {
            'dateTime': date
            # Skip many to many
        }
        self.run = Run.objects.create(**self.runAttribs)

        self.logAttribs = {
            'dateTime': date,
            'robot': self.robot,
            'run': self.run,
            'log': {
                'test': 'test text',
            }
        }
        self.log = Log.objects.create(**self.logAttribs)
        self.serializer = serializers.LogSerializer(instance=self.log)
        self.data = self.serializer.data

    def testContainsExpectedFields(self):
        self.assertEqual(set(self.data.keys()), set(self.logAttribs))