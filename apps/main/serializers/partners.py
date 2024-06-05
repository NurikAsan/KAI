from rest_framework import serializers
from ..models.partners import Partners


class PartnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partners
        fields = (
            'name',
            'image'
        )
