from core.serializers import serializers
from core.models import Wiki
from django.test import TestCase


class WikiSerializerTest(TestCase):
    def setUp(self):
        self.wikiAttribs = {
            'title': 'Test title',
            # Many to many not assignable
            'briefDescription': 'A brief test description'
        }
        self.wiki = Wiki.objects.create(**self.wikiAttribs)
        self.serializer = serializers.WikiSerializer(instance=self.wiki)
        self.data = self.serializer.data

    def testContainsExpectedFields(self):
        for key in self.wikiAttribs.keys():
            self.assertIn(key, self.data.keys())

