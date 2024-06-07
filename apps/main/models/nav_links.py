from django.db import models
from ..models.main import MainPage


class NavLinks(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок',
        null=True,
        blank=True,
    )
    url = models.URLField(verbose_name='URL')
    image = models.ImageField(
        upload_to='page-generator/',
        verbose_name='Изображение'
    )
    page = models.ForeignKey(
        MainPage,
        on_delete=models.CASCADE,
        related_name="nav_links",
        verbose_name='Страница',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Навигационные ссылки'
        verbose_name_plural = 'Навигационные ссылки'
