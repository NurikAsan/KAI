from django.db import models
from .common_models import PageGenerator


class Table(models.Model):
    name = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        verbose_name="Имя таблицы"
    )
    page = models.ForeignKey(
        PageGenerator,
        on_delete=models.CASCADE,
        verbose_name="Страница"
    )

    class Meta:
        verbose_name = "Таблица"
        verbose_name_plural = "Таблицы"


class TableCodeColumn(models.Model):
    code = models.PositiveIntegerField(
        verbose_name='Код таблицы',
        null=True,
        blank=True
    )
    year = models.PositiveIntegerField(
        default=2000,
        verbose_name='Учебный год',
        null=True,
        blank=True
    )
    table = models.ForeignKey(
        Table,
        on_delete=models.CASCADE,
        null=True,
        related_name='table_codes_column'
    )

    class Meta:
        verbose_name = "Код и Учебный план таблицы"
        verbose_name_plural = "Код и Учебный план таблицы"


class TableDirectionColumn(models.Model):
    direction = models.TextField(
        max_length=200,
        verbose_name='Направление',
    )
    status1 = models.CharField(
        max_length=100,
    )
    status2 = models.CharField(
        max_length=100,
    )
    links = models.FileField(
        upload_to='page-generator/',
        null=True,
        blank=True,
        verbose_name='Pdf файл'
    )
    table_code_column = models.ForeignKey(
        TableCodeColumn,
        on_delete=models.CASCADE,
        related_name='table_directions_column'
    )

    class Meta:
        verbose_name = "Направление таблицы и pdf файлы"
        verbose_name_plural = "Направление таблицы и pdf файлы"
