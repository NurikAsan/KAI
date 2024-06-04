from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *
from mixins.translations_mixins import TranslatorMediaMixin

TEXT = "Здесь вам нужно будет ввести данные товара на 3 разных языках"


class PostAdminForm(forms.ModelForm):
    description_ru = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    description_en = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    description_ky = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = TextContent
        fields = '__all__'


class NavLinksImageInline(admin.TabularInline):
    model = NAVImages
    max_num = 20
    extra = 0


@admin.register(NavLinks)
class NavLinksAdminModel(TranslatorMediaMixin):
    inlines = [NavLinksImageInline, ]
    list_display = ['id', "title", ]
    list_display_links = ("id",)
    list_filter = ['id', "title"]
    search_fields = ['id', "title"]


class TextContentImageInline(admin.TabularInline):
    model = Images
    max_num = 20
    extra = 0


@admin.register(TextContent)
class TextContentAdminModel(TranslatorMediaMixin):
    inlines = [TextContentImageInline, ]
    list_display = ['id', "title", 'description']
    list_display_links = ("id",)
    list_filter = ['id', "title"]
    search_fields = ['id', "title"]


class VeteranImageInline(admin.TabularInline):
    model = VeteransImages
    max_num = 20
    extra = 0


@admin.register(Veteran)
class VeteranAdminModel(TranslatorMediaMixin):
    inlines = [VeteranImageInline, ]
    list_display = ['id', "title", 'description', 'full_name', 'rank',]
    list_display_links = ("id",)
    list_filter = ['id', "title"]
    search_fields = ['id', "title"]


class PartnersInline(admin.TabularInline):
    model = PartnersImages
    max_num = 20
    extra = 0


@admin.register(Partners)
class PartnersAdminModel(TranslatorMediaMixin):
    inlines = [PartnersInline, ]
    list_display = ['id', "name", 'text']
    list_display_links = ("id",)
    list_filter = ['id', "name"]
    search_fields = ['id', "name"]


class NewsInline(admin.TabularInline):
    model = NewsImages
    max_num = 20
    extra = 0


@admin.register(News)
class NewsAdminModel(TranslatorMediaMixin):
    inlines = [NewsInline, ]
    list_display = ['id', "title", 'text']
    list_display_links = ("id",)
    list_filter = ['id', "title"]
    search_fields = ['id', "title"]


from .models.person import *
from .models.table import *
from .models.common_models import *

admin.site.register(Person)
admin.site.register(PhoneNumber)
admin.site.register(Table)
admin.site.register(TableCodeColumn)
admin.site.register(TableDirectionColumn)
admin.site.register(PageGenerator)
