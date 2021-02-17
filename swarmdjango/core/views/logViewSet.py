from django_filters.rest_framework import DjangoFilterBackend
from core.models import Log
from core.serializers import serializers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, MultiPartParser
from django.views.decorators.gzip import gzip_page
from rest_framework import status
from zipfile import ZipFile


class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = serializers.LogSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['dateTime', 'robot', 'run']
    # parser_classes = [MultiPartParser]

    # Method to accept the log file upload from the GCS
    @gzip_page
    @action(methods=['post'], detail=False)
    def upload_log_zip(self, request):
        # file_obj = request.data['file']
        with open('upload.zip', 'wb+') as destination:
            for chunk in request.FILES['file'].chunks():
                destination.write(chunk)

        with ZipFile('upload.zip') as upload:
            return Response({"Message": "Uploaded."})
        
