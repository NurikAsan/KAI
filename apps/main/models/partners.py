from django.core.paginator import Page
from django.db import models

from apps.main.models.main import MainPage
from utils.fields import WEBPField, image_folder


class Partners(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя/Название')
    image = WEBPField(upload_to=image_folder)
    link = models.URLField(verbose_name='Ссылка на сайт')
    page = models.ForeignKey(
        MainPage,
        on_delete=models.CASCADE,
        related_name='partners',
        verbose_name='Ссылка на главную страницу'
    )

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'

    def __str__(self):
        return self.name
