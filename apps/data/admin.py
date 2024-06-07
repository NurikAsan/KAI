from django.contrib import admin
from .models.news import News, NewsImages
from .models.advertisements import Advertisements, AdvertisementsImages

from modeltranslation.admin import TranslationAdmin

class TranslatorMediaMixin(TranslationAdmin):
    class Media:
        js = (
            "https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
            "adminsortable2/js/plugins/admincompat.js",
            "adminsortable2/js/libs/jquery.ui.core-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.widget-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.mouse-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.touch-punch-0.2.3.js",
            "adminsortable2/js/libs/jquery.ui.sortable-1.11.4.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }


class NewsInline(admin.TabularInline):
    model = NewsImages
    max_num = 20
    extra = 2


@admin.register(News)
class NewsAdminModel(TranslatorMediaMixin):
    inlines = (NewsInline, )
    list_display = ('id', "title", 'text')
    list_display_links = ("id",)
    list_filter = ('id', "title")
    search_fields = ('id', "title")


class AdvertisementsImagesInline(admin.TabularInline):
    model = AdvertisementsImages
    max_num = 20
    extra = 2


@admin.register(Advertisements)
class AdvertisementsAdmin(TranslatorMediaMixin):
    inlines = (AdvertisementsImagesInline, )
    list_display = ('id', "title", 'text')
    list_display_links = ("id",)
    list_filter = ('id', "title")
    search_fields = ('id', "title")
