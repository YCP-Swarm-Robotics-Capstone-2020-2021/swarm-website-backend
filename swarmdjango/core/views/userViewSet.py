from rest_framework.decorators import action
from rest_framework.response import Response

from core.models import User
from core.serializers import serializers
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
