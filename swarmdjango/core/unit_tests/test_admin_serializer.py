from django.test import TestCase
from core.models import Admin
from core.serializers.Serializers import AdminSerializer


class AdminSerializerTest(TestCase):
    def setUp(self):

        self.admin_attributes = {
            'receiveUpdates': False
        }
        self.admin = Admin.objects.create(**self.admin_attributes)
        self.serializer = AdminSerializer(instance=self.admin)

    def test_contains_fields(self):
        data = self.serializer.data

        self.assertEqual(set(data.keys()), {'receiveUpdates'})


