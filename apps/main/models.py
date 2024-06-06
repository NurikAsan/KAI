from django.db import models

# Create your models here.
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





# from rest_framework.serializers import ModelSerializer
# from rest_framework import serializers
# from .models import *
#
#
# class NewsSerializer(ModelSerializer):
#     images = serializers.SerializerMethodField("get_image")
#
#     def get_image(self, obj):
#         return NewsImageSerializer(obj.images.all(), many=True).data
#
#     class Meta:
#         model = TextContent
#         fields = ['id', 'title', 'description', 'images']
#
#
# class PartnersSerializer(ModelSerializer):
#     images = serializers.SerializerMethodField("get_image")
#
#     def get_image(self, obj):
#         return PartnerImageSerializer(obj.images.all(), many=True).data
#
#     class Meta:
#         model = Partners
#         fields = ['id', 'name', 'text', 'images']
#
#
# class NavImageSerializer(ModelSerializer):
#
#     class Meta:
#         model = NAVImages
#         fields = ["image"]
#
#
# class PartnerImageSerializer(ModelSerializer):
#
#     class Meta:
#         model = PartnersImages
#         fields = ["image"]
#
#
# class NewsImageSerializer(ModelSerializer):
#
#     class Meta:
#         model = NewsImages
#         fields = ["image"]