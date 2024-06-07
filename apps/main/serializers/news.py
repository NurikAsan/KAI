from rest_framework import serializers
from ..models.news import NewsImages, News


class NewsImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsImages
        fields = ("image", )


class NewsRetrieveSerializer(serializers.ModelSerializer):
    images = NewsImageSerializer(read_only=True, many=True)

    class Meta:
        model = News
        fields = (
            'title',
            'image',
            'text',
            'date',
            'images'
        )


class NewsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = (
            'id',
            'date',
            'text',
            'image'
        )
