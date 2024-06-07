from django.contrib import admin
from mixins.translations_mixins import TranslatorMediaMixin
from .models.advertisements import Advertisements, AdvertisementsImages
from .models.partners import Partners
from .models.news import News, NewsImages


@admin.register(Partners)
class PartnersAdminModel(TranslatorMediaMixin):
    list_display = ('id', "name", 'text')
    list_display_links = ("id",)
    list_filter = ('id', "name")
    search_fields = ('id', "name")


class NewsInline(admin.TabularInline):
    model = NewsImages
    max_num = 20
    extra = 0


@admin.register(News)
class NewsAdminModel(TranslatorMediaMixin):
    inlines = (NewsInline, )
    list_display = ('id', "title", 'text')
    list_display_links = ("id",)
    list_filter = ('id', "title")
    search_fields = ('id', "title")
