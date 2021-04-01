from core.serializers import serializers
from core.models import SideBar
from django.test import TestCase

class SideBarSerializerTest(TestCase):
    def setUp(self):
        self.sideBarAttribs = {
            'id': 0,
            'content': {
                'content': 'content'
            }
        }
        self.sideBar = SideBar.objects.create(**self.sideBarAttribs)
        self.serializer = serializers.SideBarSerializer(instance=self.sideBar)
        self.data = self.serializer.data

    def testContainsExpectedFields(self):
        self.assertEqual(set(self.data.keys()), set(self.sideBarAttribs.keys()))