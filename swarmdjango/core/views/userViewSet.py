from django.contrib.auth.hashers import check_password
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from core.serializers import serializers
from rest_framework import viewsets
from core.models import User
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

        username = self.request.query_params.get('username')
        password = self.request.query_params.get('password')
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



