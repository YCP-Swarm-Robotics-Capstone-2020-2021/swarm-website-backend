from django_filters.rest_framework import DjangoFilterBackend

from core.models import Run
from core.serializers import serializers
from rest_framework import viewsets


class RunViewSet(viewsets.ModelViewSet):
    queryset = Run.objects.all()
    serializer_class = serializers.RunSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = '__all__'