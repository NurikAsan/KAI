from ..serializers.page_generator import PageGeneratorSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..service.page_generator import PageGeneratorService


@extend_schema(tags=['PageGenerator'])
class PageGeneratorRetrieveView(APIView):

    def get(self, request, cat_id, sub_cat_id, sub_sub_cat_id=None):
        queryset = PageGeneratorService.get_pages(cat_id, sub_cat_id, sub_sub_cat_id)
        if queryset.exists():
            serializer = PageGeneratorSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "No matching records found"}, status=status.HTTP_404_NOT_FOUND)
