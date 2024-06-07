from rest_framework import serializers
from ..models.advertisements import Advertisements, AdvertisementsImages


class AdvertisementsImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdvertisementsImages
        fields = ("image", )


class AdvertisementSerializer(serializers.ModelSerializer):
    images = AdvertisementsImagesSerializer(read_only=True, many=True)

    class Meta:
        model = Advertisements
        fields = (
            'title',
            'image',
            'text',
            'date',
            'images',
        )


class AdvertisementListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advertisements
        fields = (
            'id',
            'date',
            'text',
            'image'
        )
