from django.shortcuts import render

# Create your views here.
# from rest_framework import filters, generics, views, status
# from .models import *
# from .serializers import *
# from drf_spectacular.utils import extend_schema
# from mixins.cache_mixin import CacheMixin
#
#
# @extend_schema(tags=['News'])
# # class NewsView(CacheMixin, generics.ListAPIView, generics.RetrieveAPIView):
# class NewsView(generics.ListAPIView, generics.RetrieveAPIView):
#     # CACHE_KEY_PREFIX = "news"
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer
#
#
# @extend_schema(tags=['Nav - Image'])
# # class NavImageViewSet(CacheMixin, generics.ListAPIView):
# class NavImageViewSet(generics.ListAPIView):
#     # CACHE_KEY_PREFIX = "nav_links_images"
#     queryset = NAVImages.objects.all()
#     serializer_class = NavImageSerializer
#
#
# @extend_schema(tags=['News - Image'])
# # class NewsImageViewSet(CacheMixin, generics.ListAPIView):
# class NewsImageViewSet(generics.ListAPIView):
#     # CACHE_KEY_PREFIX = "news_images"
#     queryset = NewsImages.objects.all()
#     serializer_class = NewsImageSerializer
#
#
# @extend_schema(tags=['Partner - Image'])
# # class PartnerImageViewSet(CacheMixin, generics.ListAPIView):
# class PartnerImageViewSet(generics.ListAPIView):
#     # CACHE_KEY_PREFIX = "partners_images"
#     queryset = PartnersImages.objects.all()
#     serializer_class = PartnerImageSerializer