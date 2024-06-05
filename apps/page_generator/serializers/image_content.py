from rest_framework import serializers
from apps.page_generator.models.image_content import ImageContent


class ImageContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageContent
        fields = ('image',)
