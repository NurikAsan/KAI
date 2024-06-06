from rest_framework.generics import RetrieveAPIView
from ..services.news import NewsService
from ..serializers.news import NewsRetrieveSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['Main Page'])
class NewsRetrieveAPIView(RetrieveAPIView):
    queryset = NewsService.get_new()
    serializer_class = NewsRetrieveSerializer
