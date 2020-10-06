from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from core.models import User
from core.serializers import serializers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = '__all__'

    @action(detail=False)
    def verify_password(self, request):
        obj = request.data
        obj2 = self.request.data
        obj3 = self.request.query_params.get('username')
        queryset = User.objects.all()
        user = queryset.filter(username=obj3)
        serialzer = serializers.UserSerializer(user[0])

        return Response(serialzer.data, status=status.HTTP_200_OK)

