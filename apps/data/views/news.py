from rest_framework.generics import RetrieveAPIView, ListAPIView
from ..services.news import NewsService
from ..serializers.news import NewsRetrieveSerializer, NewsListSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['Data'])
class NewsRetrieveAPIView(RetrieveAPIView):
    queryset = NewsService.get_new()
    serializer_class = NewsRetrieveSerializer


@extend_schema(tags=['Data'])
class NewsListAPIView(ListAPIView):
    queryset = NewsService.get_new()
    serializer_class = NewsListSerializer
