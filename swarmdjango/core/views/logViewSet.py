import json
from datetime import datetime

from django_filters.rest_framework import DjangoFilterBackend
from core.models import Log
from core.models import Run
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
import gc
import boto3


class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = serializers.LogSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['id', 'dateTime', 'deviceID', 'filePath']

    '''
    This method accepts a zip of log files from an http POST request.
    It then writes the bytes from the request to the directory and extracts the files.
    Next it iterates through the files in the zip, stores the raw file in the S3 bucket,
    and parses the contents of the files into the scripts for visualization and the json for storage.
    '''
    @action(methods=['post'], detail=False)
    def upload_log_zip(self, request):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        zip_root = ''
        try:
            # Access S3 bucket via the boto3 library. Credentials stored in the env file
            s3 = boto3.resource('s3',
                                aws_access_key_id=config('AWS_ACCESS_KEY'),
                                aws_secret_access_key=config('AWS_SECRET_ACCESS_KEY'))

            # Write the request bytes to destination of 'upload.zip'
            with open('upload.zip', 'wb+') as destination:
                for chunk in request.FILES['file'].chunks():
                    destination.write(chunk)

            # Open and begin processing the uploaded files
            with ZipFile('upload.zip', 'r') as upload:

                # Extract the zip file to access the files
                upload.extractall()

                # The log files will be under a common 'root' directory
                zip_root = upload.namelist()[0]

                # Walk through the upper most directory
                for root, directories, files in os.walk(os.path.join(base_dir, '../' + zip_root)):
                    for directory in directories:
                        # At this point, dir_root contains the path of zip root and directory
                        for dir_root, dirs, dir_files in os.walk(os.path.join(base_dir, '../' + zip_root + directory)):
                            # Iterate through each file in the zip files
                            for dir_file in dir_files:
                                # We are only interested in processing and storing the moos, alog, and script files
                                # We want to store raw versions of these types of files in the S3 bucket

                                if '._moos' in dir_file:
                                    # Store raw file in S3
                                    # Open the file as binary data
                                    with open(os.path.join(base_dir, dir_root + '/' + dir_file), 'rb') as file_data:
                                        # Place the file in the bucket
                                        s3.Bucket('swarm-logs-bucket').put_object(Key='{}{}{}'.format(zip_root, directory+'/', dir_file), Body=file_data)

                                # If the file is .alog it needs to be parsed into json and stored in the db
                                if '.alog' in dir_file:

                                    # Store in S3 bucket
                                    with open(os.path.join(base_dir, dir_root + '/' + dir_file), 'rb') as file_data:

                                        # Place the un-parsed file in the bucket
                                        s3.Bucket('swarm-logs-bucket').put_object(Key='{}{}{}'.format(zip_root, directory+'/', dir_file), Body=file_data)

                                        # Parse into json
                                        # Web parser return json objects that contain metadata for the log and run objects
                                        # Basically only what you need to put in the database, and enough to get the files on the S3
                                        json_obj, runs_obj = parsers.web_parser(os.path.join(base_dir, dir_root + '/' + dir_file))
                                        index_json_obj = json.loads(json_obj)
                                        index_runs = json.loads(runs_obj)

                                        # Create pieces of objects to store them in the DB
                                        device_id = index_json_obj['device_id']
                                        file_path = zip_root + directory + '/' + dir_file + '.json'
                                        # print(file_path)
                                        date = index_json_obj['date']
                                        time = index_json_obj['time']

                                        # TODO specify timezone
                                        date_time = datetime.strptime(date + ' ' + time, '%d-%m-%Y %H:%M:%S')

                                        # Create the log object first, so it can be used in the run objects
                                        log_obj = Log(dateTime=date_time, deviceID=device_id, filePath=file_path)
                                        log_obj.save()

                                        # Iterate through the returned runs and store each in the DB
                                        for i in index_runs:
                                            run_id = i['run_id']

                                            # This is the filepath the will be on the bucket
                                            run_fp = zip_root + directory+'/' + dir_file + f'-run{run_id}.json'

                                            # Save the run data to db
                                            run_obj = Run(dateTime=date_time, deviceID=device_id, runID=run_id, logID=log_obj, filePath=run_fp)
                                            run_obj.save()

                                            run_file_path = os.path.join(base_dir, dir_root + '/' + dir_file + f'-run{run_id}.json')

                                            # Upload run json to bucket
                                            with open(run_file_path, 'rb') as run_file:
                                                s3.Bucket('swarm-logs-bucket').put_object(Key='{}{}{}'.format(zip_root, directory + '/', run_file.name.split('/')[-1]), Body=run_file)

                                            # Upload the script files to the bucket
                                            if 'Narwhal' in run_file_path:
                                                run_script_path = run_file_path.replace('.json', '') + '.script'
                                                with open(run_script_path, 'rb') as script_file:
                                                    s3.Bucket('swarm-logs-bucket').put_object(Key='{}{}{}'.format(zip_root, directory + '/', script_file.name.split('/')[-1]), Body=script_file)
                                                    script_file.seek(0)
                                                    s3.Bucket('swarm-robotics-visualization').put_object(Key='scripts/{}{}{}'.format(zip_root, directory + '/', script_file.name.split('/')[-1]), Body=script_file)
                                    # Open and place the parsed json file in the bucket
                                    with open(os.path.join(base_dir, dir_root + '/' + dir_file + '.json'), 'rb') as json_file:
                                        s3.Bucket('swarm-logs-bucket').put_object(Key='{}{}{}'.format(zip_root, directory + '/', json_file.name.split('/')[-1]),Body=json_file)
        except Exception as e:
            return Response({"Status": "Upload Failed. {}".format(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            # Return the 200 response
            return Response({"Status": "Uploaded Successfully."}, status=status.HTTP_200_OK)
        finally:
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