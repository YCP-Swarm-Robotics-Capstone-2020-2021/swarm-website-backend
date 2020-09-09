from django_filters.rest_framework import DjangoFilterBackend

from core.models import Robot
from core.serializers import serializers
from rest_framework import viewsets


class RobotViewSet(viewsets.ModelViewSet):
    queryset = Robot.objects.all()
    serializer_class = serializers.RobotSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = '__all__'
