# from typing import Any
# from django.db import models
# from utils.fields import WEBPField, image_folder



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