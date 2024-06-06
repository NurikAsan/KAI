from rest_framework.generics import ListAPIView
from ..serializers.page_generator import CategoryListSerializer
from drf_spectacular.utils import extend_schema
from ..service.category import CategoryService


@extend_schema(tags=['Categories'])
class CategoriesListView(ListAPIView):
    queryset = CategoryService.get_categories()
    serializer_class = CategoryListSerializer
