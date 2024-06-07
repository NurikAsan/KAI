from rest_framework.generics import RetrieveAPIView
from ..services.advertisements import AdvertisementsService
from ..serializers.advertisements import AdvertisementSerializer


class AdvertisementsRetrieveView(RetrieveAPIView):
    queryset = AdvertisementsService.get_advertisement()
    serializer_class = AdvertisementSerializer
