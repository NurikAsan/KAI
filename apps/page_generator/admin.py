from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.core.paginator import Page

from .models.person import Person, PhoneNumber
from .models.documents import Documents
from .models.image_content import ImageContent
from .models.nav_links import *
from mixins.translations_mixins import TranslatorMediaMixin
from .models.text_content import TextContent, TextContentImages
from .models.veteran import VeteranPosition, Veteran
from .models.table import *
from .models.common_models import *


TEXT = "Здесь вам нужно будет ввести данные товара на 3 разных языках"


class PostAdminForm(forms.ModelForm):
    description_ru = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    description_en = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    description_ky = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = TextContent
        fields = '__all__'


@admin.register(NavLinks)
class NavLinksAdminModel(TranslatorMediaMixin):
    list_display = ('id', "title", )
    list_display_links = ("id",)
    list_filter = ('id', "title")
    search_fields = ('id', "title")
    raw_id_fields = ('page', )


class TextContentImageInline(admin.TabularInline):
    model = TextContentImages
    max_num = 20
    extra = 0


@admin.register(TextContent)
class TextContentAdminModel(TranslatorMediaMixin):
    inlines = [TextContentImageInline, ]
    list_display = ('id', "title", 'description')
    list_display_links = ("id",)
    list_filter = ('id', "title")
    search_fields = ('id', "title")
    raw_id_fields = ('page',)


@admin.register(ImageContent)
class ImageContent(admin.ModelAdmin):
    search_fields = ('id', )
    raw_id_fields = ('page',)


@admin.register(Documents)
class DocumentsAdmin(TranslatorMediaMixin):
    search_fields = ('id', )
    raw_id_fields = ('page', )


class PhoneNumberInline(admin.TabularInline):
    model = PhoneNumber
    extra = 2


@admin.register(Person)
class PersonAdmin(TranslatorMediaMixin):
    search_fields = ('full_name', 'position', 'email')
    raw_id_fields = ('page', )
    inlines = (PhoneNumberInline, )


class VeteranPositionInline(admin.TabularInline):
    model = VeteranPosition
    extra = 2


@admin.register(Veteran)
class VeteranAdminModel(TranslatorMediaMixin):
    inlines = (VeteranPositionInline, )
    list_display = ('id', 'full_name',)
    list_display_links = ("id",)
    list_filter = ('id',)
    search_fields = ('id', "full_name", )


@admin.register(PageGenerator)
class PageGeneratorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Table)
admin.site.register(TableCodeColumn)
admin.site.register(TableDirectionColumn)


@admin.register(Category)
class CategoryAdmin(TranslatorMediaMixin):
    pass


admin.site.register(SubCategory)
admin.site.register(SubSubCategory)
