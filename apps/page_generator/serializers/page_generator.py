from rest_framework import serializers
from ..models.common_models import PageGenerator, Category, SubCategory, SubSubCategory
from .person import PersonSerializer
from .tables import TableSerializer
from .nav_links import NavLinksSerializer
from .text_content import TextContentSerializer
from .image_content import ImageContentSerializer
from .documents import DocumentsSerializer
from .veteran import VeteranSerializer


class SubSubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubSubCategory
        fields = (
            'id',
            'name',
        )


class SubCategorySerializer(serializers.ModelSerializer):
    sub_sub_categories = SubSubCategorySerializer(read_only=True, many=True)

    class Meta:
        model = SubCategory
        fields = (
            'id',
            'name',
            'sub_sub_categories'
        )


class CategoryListSerializer(serializers.ModelSerializer):
    sub_categories = SubCategorySerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'sub_categories'
        )


class PageGeneratorSerializer(serializers.ModelSerializer):
    peoples = PersonSerializer(many=True, read_only=True)
    table = TableSerializer(read_only=True, many=True)
    nav_links = NavLinksSerializer(read_only=True, many=True)
    text_contents = TextContentSerializer(read_only=True, many=True)
    images_content = ImageContentSerializer(read_only=True, many=True)
    documents = DocumentsSerializer(read_only=True, many=True)
    veterans = VeteranSerializer(read_only=True, many=True)

    class Meta:
        model = PageGenerator
        fields = (
            'title',
            'image',
            'nav_links',
            'text_contents',
            'images_content',
            'peoples',
            'veterans',
            'table',
            'documents'
        )
