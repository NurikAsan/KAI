# from rest_framework import filters, generics, views, status
# from .models import *
# from .serializers import *
# from drf_spectacular.utils import extend_schema
# from mixins.cache_mixin import CacheMixin
#
#
#
#
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
# @extend_schema(tags=['Text - Image'])
# # class ImageViewSet(CacheMixin, generics.ListAPIView):
# class ImageViewSet(generics.ListAPIView):
#     # CACHE_KEY_PREFIX = "images"
#     queryset = Images.objects.all()
#     serializer_class = TextContentImageSerializer
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
#
#
# @extend_schema(tags=['Veteran - Image'])
# # class VeteranImageViewSet(CacheMixin, generics.ListAPIView):
# class VeteranImageViewSet(generics.ListAPIView):
#     # CACHE_KEY_PREFIX = "veteran_images"
#     queryset = VeteransImages.objects.all()
#     serializer_class = VeteranImageSerializer