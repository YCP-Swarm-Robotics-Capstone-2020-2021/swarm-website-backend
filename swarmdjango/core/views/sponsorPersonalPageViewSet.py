from django_filters.rest_framework import DjangoFilterBackend

from core.models import SponsorPersonalPage
from core.serializers import serializers
from rest_framework import viewsets


class SponsorPersonalPageViewSet(viewsets.ModelViewSet):
    queryset = SponsorPersonalPage.objects.all()
    serializer_class = serializers.SponsorPersonalPageSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = '__all__'
