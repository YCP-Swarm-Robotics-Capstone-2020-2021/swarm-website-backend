from django_filters.rest_framework import DjangoFilterBackend

from core.models import Run
from core.serializers import serializers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response


class RunViewSet(viewsets.ModelViewSet):
    queryset = Run.objects.all()
    serializer_class = serializers.RunSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['id', 'dateTime', 'deviceID', 'runID', 'logID']

    @action(methods=['get'], detail=False)
    def get_run_json(self, request):
        queryset = Run.objects.all()
        run_id = request.query_params.get('id')
        try:
            run_obj = queryset.filter(id=run_id)[0]
            serialized_run = serializers.RunSerializer(run_obj, fields=('id', 'dateTime', 'deviceID', 'runID', 'logID', 'run'))
        except IndexError:
            return Response({"Error": "Record does not exist"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"Success": serialized_run.data}, status=status.HTTP_200_OK)
