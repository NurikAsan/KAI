from django.db import models
from utils.fields import WEBPField, image_folder
from .abstract_model import AbstractModel


class Advertisements(AbstractModel):

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class AdvertisementsImages(models.Model):
    advertisement = models.ForeignKey(Advertisements, related_name='images', on_delete=models.CASCADE, verbose_name='Ссылка на объявления')
    image = WEBPField(upload_to=image_folder, verbose_name='Изображение')
