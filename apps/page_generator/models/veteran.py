from django.db import models

from apps.page_generator.models.common_models import PageGenerator


class Veteran(models.Model):
    full_name = models.CharField(
        max_length=100,
        verbose_name="Полное имя"
    )
    image = models.ImageField(
        upload_to='page-generator/veterans',
        null=False,
        blank=False,
        verbose_name="Изображение"
    )
    page = models.ForeignKey(
        PageGenerator,
        on_delete=models.SET_NULL,
        related_name='veterans',
        null=True,
        blank=True,
        verbose_name="Страница"
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Ветеран"
        verbose_name_plural = "Ветераны"


class VeteranPosition(models.Model):
    position = models.CharField(
        max_length=150,
        verbose_name="Должность",
        null=True,
        blank=True
    )
    veteran = models.ForeignKey(
        Veteran,
        on_delete=models.CASCADE,
        related_name='veteran_positions',
        verbose_name="Ветеран",
    )
