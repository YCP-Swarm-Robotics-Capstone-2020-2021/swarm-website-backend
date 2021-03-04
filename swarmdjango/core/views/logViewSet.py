from django_filters.rest_framework import DjangoFilterBackend
from core.models import Log
from core.serializers import serializers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from core.logParsers import parsers
from rest_framework import status
from zipfile import ZipFile
from decouple import config
import os
import shutil
import boto3


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
    '''
    @action(methods=['post'], detail=False)
    def upload_log_zip(self, request):
        s3 = boto3.resource('s3',
                            aws_access_key_id=config('AWS_ACCESS_KEY'),
                            aws_secret_access_key=config('AWS_SECRET_ACCESS_KEY'))

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # Write the request bytes to destination of 'upload.zip'
        with open('upload.zip', 'wb+') as destination:
            for chunk in request.FILES['file'].chunks():
                destination.write(chunk)

        # Open and begin processing the uploaded files
        zip_root = ''
        with ZipFile('upload.zip', 'r') as upload:
            # Extract the zip file to access the files
            upload.extractall()
            # The log files will be under a common 'root' directory
            zip_root = upload.namelist()[0]
            print('Processing logs')
            # Walk through the upper most directory
            for root, directories, files in os.walk(os.path.join(base_dir, '../' + zip_root)):
                # Iterate through each file in the zip files
                for file in files:
                    # We are only interested in processing and storing the moos, alog, and script files
                    # We want to store raw versions of these types of files in the S3 bucket
                    if '._moos' in file:
                        # TODO Store raw file in S3
                        # Open the file as binary data
                        file_data = open(root + '/' + file, 'rb')
                        # Place the file in the bucket
                        s3.Bucket('swarm-logs-bucket').put_object(Key='{}{}'.format(zip_root, file), Body=file_data)

                    # If the file is .alog it needs to be parsed into json and stored in the db
                    elif '.alog' in file:
                        # Narwhal alog needs to be parsed for visualization
                        if 'Narwhal' in file:
                            # TODO Parse for visualization
                            parsers.visualization_parser(os.path.join(root + '/', file))
                            # TODO Store visualization script in S3 bucket
                            script_data = open(root + '/' + file + '.script', 'rb')
                            # Note that the script name must be split on / to isolate just the script name and not the
                            # Directory structure
                            s3.Bucket('swarm-logs-bucket').put_object(Key='{}{}'.format(zip_root, script_data.name.split('/')[-1]), Body=script_data)
                            # print('Parsed for visualization')
                        # Store in S3 bucket
                        file_data = open(root + '/' + file, 'rb')
                        # Place the file in the bucket
                        s3.Bucket('swarm-logs-bucket').put_object(Key='{}{}'.format(zip_root, file), Body=file_data)
                        # TODO Parse into json
                        # TODO Store database

        # Clean up the files and directories that get created
        try:
            os.remove(os.path.join(base_dir, '../upload.zip'))
        except OSError as error:
            print('Error removing upload.zip \n' + error)
        if zip_root != '':
            shutil.rmtree(os.path.join(base_dir, '../' + zip_root))

        # Walk the directory above to make sure the __MACOSX directory gets deleted if it is created
        for root, directories, files in os.walk(os.path.join(base_dir, '../')):
            if '__MACOSX' in directories:
                shutil.rmtree(os.path.join(base_dir, '../__MACOSX'))
                break

        # Return the response
        return Response({"Message": "Uploaded."})

