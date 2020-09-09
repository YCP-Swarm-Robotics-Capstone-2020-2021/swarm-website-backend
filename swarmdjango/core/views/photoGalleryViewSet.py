from django_filters.rest_framework import DjangoFilterBackend

from core.models import PhotoGallery
from core.serializers import serializers
from rest_framework import viewsets


class PhotoGalleryViewSet(viewsets.ModelViewSet):
    queryset = PhotoGallery.objects.all()
    serializer_class = serializers.UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = '__all__'
