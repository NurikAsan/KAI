from django.db import models
from utils.fields import WEBPField, image_folder
from .abstract_model import AbstractModel


class News(AbstractModel):

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class NewsImages(models.Model):
    news = models.ForeignKey(News, related_name='images', on_delete=models.CASCADE, verbose_name='Ссылка на новости')
    image = WEBPField(upload_to=image_folder, verbose_name='Изображение')
