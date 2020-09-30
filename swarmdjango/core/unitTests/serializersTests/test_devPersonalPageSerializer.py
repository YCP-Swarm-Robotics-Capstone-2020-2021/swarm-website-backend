from core.serializers import serializers
from core.models import DevPersonalPage
from django.test import TestCase


class DevPersonalPageSerializerTest(TestCase):

    def setUp(self):
        self.devPersonalPageAttribs = {
            'expectedGraduationYear': 2021,
            'biography': 'Test Dev Page bio',
            'motivationForWorking': 'I like software engineer',
            # Many to many not assignable
        }
        self.devPersonalPage = DevPersonalPage.objects.create(**self.devPersonalPageAttribs)
        self.serializer = serializers.DevPersonalPageSerializer(instance=self.devPersonalPage)
        self.data = self.serializer.data

    def testContainsExpectedFields(self):
        for key in self.devPersonalPageAttribs:
            self.assertIn(key, self.data.keys())
