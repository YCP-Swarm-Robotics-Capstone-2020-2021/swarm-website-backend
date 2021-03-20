from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from core.models import Entry
from core.serializers import serializers
from rest_framework import viewsets, status


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = serializers.EntrySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = '__all__'

    @action(detail=False)
    def delete_entry(self, request, *args, **kwargs):
        id = self.request.query_params.get('id')
        entry_to_delete = get_object_or_404(Entry, id=id)

        # delete associated models, then the entry
        entry_to_delete.log.all().delete()
        entry_to_delete.comments.all().delete()
        entry_to_delete.headings.all().delete()
        entry_to_delete.sideBar.delete()

        entry_to_delete.delete()
        return Response(status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def get_all_changes(self, request):
        id = self.request.query_params.get('id')
        entry = get_object_or_404(Entry, id=id)

        # get all Change objects for the chose entry, and each of
        # its headings
        logs = (entry.log.all().values())
        for heading in entry.headings.all():
            logs = logs.union(heading.log.all().values()).order_by('-id')

        return Response(logs, status=status.HTTP_200_OK);