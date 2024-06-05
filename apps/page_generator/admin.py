from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models.documents import Documents
from .models.image_content import ImageContent
from .models.nav_links import *
from mixins.translations_mixins import TranslatorMediaMixin
from .models.text_content import TextContent, TextContentImages


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
    model = ImageContent
    search_fields = ('id', )
    raw_id_fields = ('page',)


@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    model = Documents
    search_fields = ('id', )
    raw_id_fields = ('page', )

# class VeteranImageInline(admin.TabularInline):
#     model = VeteransImages
#     max_num = 20
#     extra = 0
#
#
# @admin.register(Veteran)
# class VeteranAdminModel(TranslatorMediaMixin):
#     inlines = [VeteranImageInline, ]
#     list_display = ['id', "title", 'description', 'full_name', 'rank',]
#     list_display_links = ("id",)
#     list_filter = ['id', "title"]
#     search_fields = ['id', "title"]
#
#
# class PartnersInline(admin.TabularInline):
#     model = PartnersImages
#     max_num = 20
#     extra = 0
#
#
# @admin.register(Partners)
# class PartnersAdminModel(TranslatorMediaMixin):
#     inlines = [PartnersInline, ]
#     list_display = ['id', "name", 'text']
#     list_display_links = ("id",)
#     list_filter = ['id', "name"]
#     search_fields = ['id', "name"]
#
#
# class NewsInline(admin.TabularInline):
#     model = NewsImages
#     max_num = 20
#     extra = 0
#
#
# @admin.register(News)
# class NewsAdminModel(TranslatorMediaMixin):
#     inlines = [NewsInline, ]
#     list_display = ['id', "title", 'text']
#     list_display_links = ("id",)
#     list_filter = ['id', "title"]
#     search_fields = ['id', "title"]

from .models.person import *
from .models.table import *
from .models.common_models import *

admin.site.register(Person)
admin.site.register(PhoneNumber)
admin.site.register(Table)
admin.site.register(TableCodeColumn)
admin.site.register(TableDirectionColumn)
admin.site.register(PageGenerator)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(SubSubCategory)
