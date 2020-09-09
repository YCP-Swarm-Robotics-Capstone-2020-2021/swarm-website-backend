from django_filters.rest_framework import DjangoFilterBackend

from core.models import Change
from core.serializers import serializers
from rest_framework import viewsets


class ChangeViewSet(viewsets.ModelViewSet):
    queryset = Change.objects.all()
    serializer_class = serializers.ChangeSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = '__all__'
