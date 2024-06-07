from apps.main.models.advertisements import Advertisements


class AdvertisementsService:
    @staticmethod
    def get_advertisement():
        return Advertisements.objects.all()
