from django_filters.rest_framework import DjangoFilterBackend

from core.models import Developer
from core.serializers import serializers
from rest_framework import viewsets


class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = serializers.DeveloperSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = '__all__'
