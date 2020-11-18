from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status

from core.models import Wiki
from core.serializers import serializers
from rest_framework import viewsets


class WikiViewSet(viewsets.ModelViewSet):
    queryset = Wiki.objects.all()
    serializer_class = serializers.WikiSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = '__all__'

    @action(detail=False)
    def get_last_updated(self, request, *args, **kwargs):
        id = self.request.query_params.get('id')

        wiki_to_read = get_object_or_404(Wiki, id=id)
        entries = wiki_to_read.entries.all()

        if len(entries) == 0:
            return Response({"date": "N/A"}, status=status.HTTP_200_OK)

        latest = entries.latest()
        date_time = latest.log.latest().dateTime

        return Response({"date": date_time}, status=status.HTTP_200_OK)

    @action(detail=False)
    def delete_wiki(self, request, *args, **kwargs):
        id = self.request.query_params.get('id')
        wiki_to_delete = get_object_or_404(Wiki, id=id)

        # delete associated models (entries), then the wiki
        entries = wiki_to_delete.entries.all()
        for entry in entries:
            entry.log.all().delete()
            entry.comments.all().delete()
            entry.headings.all().delete()
            entry.sideBar.delete()

        wiki_to_delete.delete()
        return Response(status=status.HTTP_200_OK)