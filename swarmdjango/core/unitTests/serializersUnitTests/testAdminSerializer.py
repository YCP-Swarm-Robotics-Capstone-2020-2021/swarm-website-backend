from django.test import TestCase
from core.models import Admin
from core.serializers.serializers import AdminSerializer


class AdminSerializerTest(TestCase):
    def setUp(self):
        # Create attributes to be passed to an admin object
        self.adminAttributes = {
            'receiveUpdates': False
        }
        # Create an admin object
        self.admin = Admin.objects.create(**self.adminAttributes)
        # Create admin serializer
        self.serializer = AdminSerializer(instance=self.admin)
        # Serializer data to test against
        self.data = self.serializer.data

    # Test serializer has correct fields
    def testContainsFields(self):
        self.assertEqual(set(self.data.keys()), {'receiveUpdates'})

    # Test that fields contain correct data
    def testAdminFieldContent(self):
        self.assertFalse(self.data['receiveUpdates'])

