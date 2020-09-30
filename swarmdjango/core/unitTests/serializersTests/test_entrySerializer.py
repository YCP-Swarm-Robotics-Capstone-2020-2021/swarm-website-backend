from core.serializers import serializers
from core.models import Entry, SideBar
from django.test import TestCase


class EntrySerializerTest(TestCase):
    def setUp(self):
        self.sideBarAttribs = {
            'content': {
                'content': 'content'
            }
        }
        self.sideBar = SideBar.objects.create(**self.sideBarAttribs)
        self.entryAttribs = {
            'title': 'Test Title',
            'text': 'Test text',
            'sideBar': self.sideBar
            # Many to many fields not tested
        }

        self.entry = Entry.objects.create(**self.entryAttribs)
        self.serializer = serializers.EntrySerializer(instance=self.entry)
        self.data = self.serializer.data

    def testContainsExpectedFields(self):
        for key in self.entryAttribs:
            self.assertIn(key, self.data.keys())