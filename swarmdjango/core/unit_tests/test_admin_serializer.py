from django.test import TestCase
from core.models import Admin
from core.serializers.Serializers import AdminSerializer


class AdminSerializerTest(TestCase):
    def setUp(self):
        # Create attributes to be passed to an admin object
        self.admin_attributes = {
            'receiveUpdates': False
        }
        # Create an admin object
        self.admin = Admin.objects.create(**self.admin_attributes)
        # Create admin serializer
        self.serializer = AdminSerializer(instance=self.admin)
        # Serializer data to test against
        self.data = self.serializer.data

    # Test serializer has correct fields
    def test_contains_fields(self):
        self.assertEqual(set(self.data.keys()), {'receiveUpdates'})

    # Test that fields contain correct data
    def test_update_field_content(self):
        self.assertFalse(self.data['receiveUpdates'])

