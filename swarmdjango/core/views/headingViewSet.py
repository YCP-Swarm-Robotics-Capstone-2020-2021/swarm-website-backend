from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from core.models import Heading
from core.serializers import serializers
from rest_framework import viewsets, status


class HeadingViewSet(viewsets.ModelViewSet):
    queryset = Heading.objects.all()
    serializer_class = serializers.HeadingSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = '__all__'

    @action(detail=False)
    def delete_heading(self, request, *args, **kwargs):
        id = self.request.query_params.get('id')
        heading_to_delete = get_object_or_404(Heading, id=id)

        # delete associated models, then the heading
        heading_to_delete.log.all().delete()
        heading_to_delete.subHeadings.all().delete()

        heading_to_delete.delete()
        return Response(status=status.HTTP_200_OK)
