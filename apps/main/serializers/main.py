from rest_framework import serializers
from ..models.main import MainPage, BannerWithText


class BannerTextSerializer(serializers.ModelSerializer):

    class Meta:
        model = BannerWithText
        fields = (
            'title',
            'image'
        )


class MainSerializer(serializers.ModelSerializer):
    banner_texts = BannerTextSerializer(read_only=True, many=True)

    class Meta:
        model = MainPage
        fields = (
            'banner_texts',
        )
