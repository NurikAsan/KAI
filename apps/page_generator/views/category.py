from rest_framework.generics import ListAPIView
from ..serializers.page_generator import CategoryListSerializer
from drf_spectacular.utils import extend_schema

from apps.page_generator.models.common_models import Category


@extend_schema(tags=['Categories'])
class CategoriesListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
