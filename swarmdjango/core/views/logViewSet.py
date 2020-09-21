from django_filters.rest_framework import DjangoFilterBackend

from core.models import Log
from core.serializers import serializers
from rest_framework import viewsets


class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = serializers.LogSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['dateTime', 'robot', 'run']
