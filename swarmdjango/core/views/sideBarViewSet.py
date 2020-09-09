from django_filters.rest_framework import DjangoFilterBackend

from core.models import SideBar
from core.serializers import serializers
from rest_framework import viewsets


class SideBarViewSet(viewsets.ModelViewSet):
    queryset = SideBar.objects.all()
    serializer_class = serializers.UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = '__all__'
