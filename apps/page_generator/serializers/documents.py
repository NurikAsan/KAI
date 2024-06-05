from rest_framework import serializers
from ..models.documents import Documents


class DocumentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Documents
        fields = (
            'pdf',
        )
