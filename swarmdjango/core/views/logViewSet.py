from django_filters.rest_framework import DjangoFilterBackend
from core.models import Log
from core.serializers import serializers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.views.decorators.gzip import gzip_page
from rest_framework import status
from zipfile import ZipFile
import os
import shutil


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
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # Write the request bytes to destination of 'upload.zip'
        with open('upload.zip', 'wb+') as destination:
            for chunk in request.FILES['file'].chunks():
                destination.write(chunk)

        # Open and begin processing the uploaded files
        with ZipFile('upload.zip', 'r') as upload:
            upload.extractall()
            zip_root = upload.namelist()[0]
            print('Processing logs')
            for root, directories, files in os.walk(os.path.join(base_dir, '../' + zip_root)):
                for file in files:
                    print(file)

        # Clean up the files and directories that get created
        os.remove(os.path.join(base_dir, '../upload.zip'))
        shutil.rmtree(os.path.join(base_dir, '../onerobotlog'))
        
        # Walk the directory above to make sure the __MACOSX directory gets deleted on my computer
        for root, directories, files in os.walk(os.path.join(base_dir, '../')):
            if '__MACOSX' in directories:
                print('Removing directory created by mac os')
                shutil.rmtree(os.path.join(base_dir, '../__MACOSX'))

        # Check the zip file CRCs
        return Response({"Message": "Uploaded."})

