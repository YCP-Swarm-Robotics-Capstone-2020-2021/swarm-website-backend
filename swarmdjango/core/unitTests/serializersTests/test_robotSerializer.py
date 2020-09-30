from core.serializers import serializers
from core.models import Robot
from django.test import TestCase


class RobotSerializerTest(TestCase):
    def setUp(self):
        self.robotAttribs = {
            'name': 'Robot1',
            'ip': '0.0.0.0'
        }
        self.robot = Robot.objects.create(**self.robotAttribs)
        self.serializer = serializers.RobotSerializer(instance=self.robot)
        self.data = self.serializer.data

    def testContainsExpectedFields(self):
        self.assertEqual(set(self.data.keys()), set(self.robotAttribs.keys()))