from django.db import models
from apps.page_generator.models.common_models import PageGenerator


class Documents(models.Model):
    name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Pdf Файл"
    )
    pdf = models.FileField(
        upload_to='page-generator/documents',
        verbose_name="Документ"
    )
    page = models.ForeignKey(
        PageGenerator,
        on_delete=models.SET_NULL,
        related_name='documents',
        blank=True,
        null=True,
        verbose_name="Страница"
    )

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"
        # indexes = ['name']
