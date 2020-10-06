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

#######################################################################
    @action(detail=False)
    def checkPassword(self):
        queryset = User.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(username=username)
            obj = False
        else:
            obj = "False"
        return Response(obj, status=status.HTTP_200_OK, template_name=None, headers=None, content_type=None)
#######################################################################
