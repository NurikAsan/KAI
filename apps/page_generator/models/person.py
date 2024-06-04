from django.db import models
from .common_models import PageGenerator


class Person(models.Model):
    full_name = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="Полное имя человека"
    )
    image = models.ImageField(
        upload_to='page-generator/',
        blank=False,
        null=False,
        verbose_name="Изображение человека"
    )
    position = models.TextField(
        max_length=150,
        null=True,
        blank=True,
        verbose_name="Должность человека"
    )
    email = models.EmailField(
        max_length=150,
        null=True,
        blank=True
    )
    faks = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        verbose_name="Факс"
    )
    page = models.ForeignKey(
        PageGenerator,
        on_delete=models.CASCADE,
        related_name='peoples',
        verbose_name="Страница"
    )


class PhoneNumber(models.Model):
    phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name="Номер телефон"
    )
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="phone_numbers",
        verbose_name="Владелец"
    )
