from django.db import models

from apps.page_generator.models.common_models import PageGenerator


class ImageContent(models.Model):
    image = models.ImageField(
        upload_to='page-generator/images',
        verbose_name="Изображение"
    )
    page = models.ForeignKey(
        PageGenerator,
        on_delete=models.SET_NULL,
        related_name='images_content',
        verbose_name="Страница",
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = 'Изображения для страниц'
