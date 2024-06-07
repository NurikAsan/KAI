from rest_framework.generics import RetrieveAPIView, ListAPIView
from ..services.advertisements import AdvertisementsService
from ..serializers.advertisements import AdvertisementSerializer, AdvertisementListSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['Data'])
class AdvertisementsRetrieveView(RetrieveAPIView):
    queryset = AdvertisementsService.get_advertisement()
    serializer_class = AdvertisementSerializer


@extend_schema(tags=['Data'])
class AdvertisementsListView(ListAPIView):
    queryset = AdvertisementsService.get_advertisement()
    serializer_class = AdvertisementListSerializer
