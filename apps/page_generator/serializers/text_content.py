from rest_framework import serializers
from ..models.text_content import TextContent, TextContentImages


class TextContentPageSerializer(serializers.ModelSerializer):

    class Meta:
        model = TextContentImages
        fields = (
            'image',
        )


class TextContentSerializer(serializers.ModelSerializer):
    text_content_images = TextContentPageSerializer(read_only=True, many=True)

    class Meta:
        model = TextContent
        fields = (
            'title',
            'description',
            'text_content_images'
        )
