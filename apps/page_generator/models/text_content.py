from django.db import models
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe

from apps.page_generator.models.common_models import PageGenerator
from utils.fields import WEBPField


class TextContent(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = RichTextField(
        null=True,
        blank=True,
        verbose_name='Текстовое описание'
    )
    page = models.ForeignKey(
        PageGenerator,
        on_delete=models.CASCADE,
        related_name='text_contents',
        null=True,
        blank=True,
        verbose_name='Страница'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Контент страниц'

    CACHE_KEY_PREFIX = "text_content"


class TextContentImages(models.Model):
    content_text = models.ForeignKey(
        TextContent,
        related_name='text_content_images',
        on_delete=models.SET_NULL,
        verbose_name='Текст',
        null=True,
        blank=True
    )
    image = WEBPField(
        upload_to='page-generator/text-content/',
        null=True,
        blank=True,
        verbose_name='Изображение'
    )

    CACHE_KEY_PREFIX = "images"

    def __str__(self):
        return mark_safe("<img src='{image.url}' width='50' >")

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображение для контента страниц'
