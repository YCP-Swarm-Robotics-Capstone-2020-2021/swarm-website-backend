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
