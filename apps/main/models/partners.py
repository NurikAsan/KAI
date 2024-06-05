from django.db import models
from utils.fields import WEBPField, image_folder


class Partners(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя/Название')
    image = WEBPField(upload_to=image_folder)

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'

    CACHE_KEY_PREFIX = "partners"

    def __str__(self):
        return self.name