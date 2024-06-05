from rest_framework import serializers
from apps.page_generator.models.veteran import Veteran, VeteranPosition


class VeteranPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = VeteranPosition
        fields = (
            'position',
        )


class VeteranSerializer(serializers.ModelSerializer):
    veteran_positions = VeteranPositionSerializer(many=True, read_only=True)

    class Meta:
        model = Veteran
        fields = (
            'full_name',
            'image',
            'veteran_positions'
        )
