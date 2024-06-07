from rest_framework import serializers
from ..models.main import MainPage, BannerWithText
from .nav_links import NavLinksSerializer
from ...data.models.news import News
from ...data.models.advertisements import Advertisements
from ...data.serializers.news import NewsListSerializer
from ...data.serializers.advertisements import AdvertisementListSerializer
from ..serializers.partners import PartnerSerializer


class BannerTextSerializer(serializers.ModelSerializer):

    class Meta:
        model = BannerWithText
        fields = (
            'title',
            'image',
        )


class MainSerializer(serializers.ModelSerializer):
    banner_texts = BannerTextSerializer(read_only=True, many=True)
    nav_links = NavLinksSerializer(read_only=True, many=True)
    advertisements = serializers.SerializerMethodField()
    news = serializers.SerializerMethodField()
    partners = PartnerSerializer(read_only=True, many=True)

    class Meta:
        model = MainPage
        fields = (
            'banner_texts',
            'nav_links',
            'news',
            'advertisements',
            'description',
            'partners'
        )

    def get_news(self, obj):
        news_items = News.objects.all()[:5]
        return NewsListSerializer(news_items, many=True).data

    def get_advertisements(self, obj):
        advertisements_item = Advertisements.objects.all()[:5]
        return AdvertisementListSerializer(advertisements_item, many=True).data
