from rest_framework.generics import ListAPIView
from ..serializers.main import MainSerializer
from drf_spectacular.utils import extend_schema
from ..services.main import MainPageService


@extend_schema(tags=['Main Page'])
class MainListAPIView(ListAPIView):
    queryset = MainPageService.get_main_content()
    serializer_class = MainSerializer
