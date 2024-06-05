# from typing import Any
# from django.db import models
# from ckeditor.fields import RichTextField
# from utils.fields import WEBPField, image_folder
#
#
# class TextContent(models.Model):
#     title = models.CharField(max_length=100, verbose_name='Заголовок')
#     description = RichTextField(null=True, blank=True)
#
#     def __str__(self):
#         return self.title
#
#     CACHE_KEY_PREFIX = "text_content"
#
#
# class Veteran(models.Model):
#     title = models.CharField(max_length=100, verbose_name="Заголовок")
#     full_name = models.CharField(max_length=150, null=False, blank=False, verbose_name="Полное имя")
#     rank = models.CharField(max_length=100, blank=True, null=True, verbose_name="Звание")
#     description = RichTextField(null=True, blank=True)
#
#     def __str__(self):
#         return self.title
#
#     CACHE_KEY_PREFIX = "veteran"
#
#     class Meta:
#         verbose_name = 'Ветеран'
#         verbose_name_plural = 'Ветераны'
#
#
# class VeteransImages(models.Model):
#     veterans = models.ForeignKey(Veteran, related_name='images', on_delete=models.CASCADE)
#     image = WEBPField(upload_to=image_folder)
#
#     CACHE_KEY_PREFIX = "veteran_images"
#
#
# class Partners(models.Model):
#     name = models.CharField(max_length=50, verbose_name='Имя/Название')
#     text = RichTextField(null=True, blank=True)
#
#     class Meta:
#         verbose_name = 'Партнер'
#         verbose_name_plural = 'Партнеры'
#
#     CACHE_KEY_PREFIX = "partners"
#
#     def __str__(self):
#         return self.name
#
#
# class PartnersImages(models.Model):
#     partners = models.ForeignKey(Partners, related_name='images', on_delete=models.CASCADE)
#     image = WEBPField(upload_to=image_folder)
#
#     CACHE_KEY_PREFIX = "partners_images"
#
#
# class News(models.Model):
#     title = models.CharField(max_length=500, verbose_name='Оглавление')
#     text = RichTextField(null=True, blank=True)
#
#     class Meta:
#         verbose_name = 'Новость'
#         verbose_name_plural = 'Новости'
#
#     CACHE_KEY_PREFIX = "news"
#
#     def __str__(self):
#         return self.title
#
#
# class NewsImages(models.Model):
#     news = models.ForeignKey(News, related_name='images', on_delete=models.CASCADE)
#     image = WEBPField(upload_to=image_folder)
#
#     CACHE_KEY_PREFIX = "news_images"
#
#
# class Images(models.Model):
#     content_text = models.ForeignKey(TextContent, related_name='images', on_delete=models.CASCADE)
#     image = WEBPField(upload_to=image_folder)
#
#     CACHE_KEY_PREFIX = "images"
