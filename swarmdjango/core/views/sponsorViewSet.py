from django_filters.rest_framework import DjangoFilterBackend

from core.models import Sponsor
from core.serializers import serializers
from rest_framework import viewsets


class SponsorViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = serializers.UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = '__all__'
