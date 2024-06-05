from rest_framework import serializers
from ..models.common_models import PageGenerator
from .person import PersonSerializer
from .tables import TableSerializer
from .nav_links import NavLinksSerializer


class PageGeneratorSerializer(serializers.ModelSerializer):
    peoples = PersonSerializer(many=True, read_only=True)
    table = TableSerializer(read_only=True, many=True)
    nav_links = NavLinksSerializer(read_only=True, many=True)

    class Meta:
        model = PageGenerator
        fields = (
            'peoples',
            'table',
            'nav_links'
        )
