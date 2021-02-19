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

    '''
    This method accepts a zip of log files from an http POST request.
    It then writes the bytes from the request to the directory and extracts the files.
    Next it iterates through the files in the zip, stores the raw file in the S3 bucket,
    and parses the contents of the files into the scripts for visualization and the json for storage.
    
    Gzip is required for parsing the body of the response from bytes to a zip file.
    '''
    @gzip_page
    @action(methods=['post'], detail=False)
    def upload_log_zip(self, request):
        # Write the request bytes to destination of 'upload.zip'
        with open('upload.zip', 'wb+') as destination:
            for chunk in request.FILES['file'].chunks():
                destination.write(chunk)

        # Open and begin processing the uploaded files
        with ZipFile('upload.zip') as upload:
            return Response({"Message": "Uploaded."})
        
