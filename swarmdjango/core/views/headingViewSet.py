from django_filters.rest_framework import DjangoFilterBackend

from core.models import Heading
from core.serializers import serializers
from rest_framework import viewsets


class HeadingViewSet(viewsets.ModelViewSet):
    queryset = Heading.objects.all()
    serializer_class = serializers.HeadingSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = '__all__'
