from ..serializers.page_generator import PageGeneratorSerializer
from ..models.common_models import PageGenerator
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status


@extend_schema(tags=['PageGenerator'])
class PageGeneratorRetrieveView(APIView):

    def get(self, request, cat_id, sub_cat_id, sub_sub_cat_id=None):
        if sub_sub_cat_id is None:
            queryset = PageGenerator.objects.filter(
                Q(category_id=cat_id) & Q(subcategory_id=sub_cat_id) & Q(subcategory2_id=sub_sub_cat_id)
            )
        else:
            queryset = PageGenerator.objects.filter(
                Q(category_id=cat_id) & (Q(subcategory_id=sub_cat_id))
            )

        if queryset.exists():
            serializer = PageGeneratorSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "No matching records found"}, status=status.HTTP_404_NOT_FOUND)
