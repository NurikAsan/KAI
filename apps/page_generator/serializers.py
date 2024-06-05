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
#
# class TextContentSerializer(ModelSerializer):
#     images = serializers.SerializerMethodField("get_image")
#
#     def get_image(self, obj):
#         return TextContentImageSerializer(obj.images.all(), many=True).data
#
#     class Meta:
#         model = TextContent
#         fields = ['id', 'title', 'description', 'images']
#
#
# class VeteranSerializer(ModelSerializer):
#     images = serializers.SerializerMethodField("get_image")
#
#     def get_image(self, obj):
#         return VeteranImageSerializer(obj.images.all(), many=True).data
#
#     class Meta:
#         model = Veteran
#         fields = ['id', 'title', 'full_name', 'rank', 'description', 'images']
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
# class VeteranImageSerializer(ModelSerializer):
#
#     class Meta:
#         model = VeteransImages
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
# class TextContentImageSerializer(ModelSerializer):
#
#     class Meta:
#         model = Images
#         fields = ["image"]
#
#
# class NewsImageSerializer(ModelSerializer):
#
#     class Meta:
#         model = NewsImages
#         fields = ["image"]