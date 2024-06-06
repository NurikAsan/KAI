from django.db import models


class MainPage(models.Model):
    pass


class BannerWithText(models.Model):
    title = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Описание Баннера'
    )
    image = models.ImageField(
        upload_to='main/',
        verbose_name='Изображение'
    )
    main = models.ForeignKey(
        MainPage,
        on_delete=models.SET_NULL,
        related_name='banner_texts',
        null=True,
        blank=True,
        verbose_name='Ссылка на главную страницу'
    )

