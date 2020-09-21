from core.models import SideBar
from core.serializers import serializers
from rest_framework import viewsets


class SideBarViewSet(viewsets.ModelViewSet):
    queryset = SideBar.objects.all()
    serializer_class = serializers.SideBarSerializer
