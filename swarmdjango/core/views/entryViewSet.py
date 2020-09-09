from django_filters.rest_framework import DjangoFilterBackend

from core.models import Entry
from core.serializers import serializers
from rest_framework import viewsets


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = serializers.EntrySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = '__all__'
