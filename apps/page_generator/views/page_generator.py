from ..serializers.page_generator import PageGeneratorSerializer
from rest_framework.generics import ListAPIView
from ..models.common_models import PageGenerator


class PageGeneratorListView(ListAPIView):
    queryset = PageGenerator.objects.all()
    serializer_class = PageGeneratorSerializer
