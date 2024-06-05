from rest_framework import serializers
from ..models.nav_links import NavLinks


class NavLinksSerializer(serializers.ModelSerializer):

    class Meta:
        model = NavLinks
        fields = ['title', 'url', 'image']
