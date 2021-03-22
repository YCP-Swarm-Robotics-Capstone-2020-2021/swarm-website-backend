import json

from django.contrib.auth.hashers import check_password
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from core.serializers import serializers
from rest_framework.decorators import action
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    filter_backends = DjangoFilterBackend
    permission_classes = [permissions.IsAuthenticated]
    filter_fields = '__all__'

    @action(methods=['post'], detail=False)
    def verify_password(self, request):

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        username = body['username']
        password = body['password']

        queryset = User.objects.all()

        user = queryset.filter(username=username)

        try:
            user_serialized = serializers.UserSerializer(user[0])
        except IndexError:
            return Response({"Error": "Record does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # Retrieve the user password from the returned object
        hash = user_serialized.data.get('password')

        if check_password(password, hash):
            return Response({"Status": True}, status=status.HTTP_200_OK)
        else:
            return Response({"Status": False, "Error": "Password was incorrect"}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False)
    def find_user(self, request):
        username = self.request.query_params.get('username')
        queryset = User.objects.all()

        user = queryset.filter(username=username)

        try:
            serializers.UserSerializer(user[0])
        except IndexError:
            return Response({"Error": "Record does not exist"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"Status": True, }, status=status.HTTP_200_OK)
