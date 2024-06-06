from rest_framework.generics import ListAPIView
from ..models.main import MainPage
from ..serializers.main import MainSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['Main Page'])
class MainListAPIView(ListAPIView):
    queryset = MainPage.objects.all()
    serializer_class = MainSerializer
