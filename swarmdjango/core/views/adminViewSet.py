from django_filters.rest_framework import DjangoFilterBackend

from core.models import Admin
from core.serializers import serializers
from rest_framework import viewsets


class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.select_related()
    serializer_class = serializers.AdminSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = '__all__'