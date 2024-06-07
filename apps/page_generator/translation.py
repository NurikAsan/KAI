from modeltranslation.translator import register, TranslationOptions

from .models.common_models import PageGenerator, Category, SubCategory, SubSubCategory
from .models.documents import Documents
from .models.nav_links import NavLinks
from .models.person import Person
from .models.table import Table, TableDirectionColumn
from .models.text_content import TextContent
from .models.veteran import Veteran, VeteranPosition


@register(NavLinks)
class NavLinksTranslateOptions(TranslationOptions):
    fields = ('title', )


@register(TextContent)
class TextContentTranslateOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(PageGenerator)
class PageGeneratorTranslateOptions(TranslationOptions):
    fields = ('title', )


@register(Person)
class PersonTranslatableOptions(TranslationOptions):
    fields = ('full_name', 'position', )


@register(Table)
class TableTranslatableOptions(TranslationOptions):
    fields = ('name', )


@register(TableDirectionColumn)
class TableDirectionColumnTranslatableOptions(TranslationOptions):
    fields = ('direction', 'status1', 'status2')


@register(Veteran)
class VeteransTranslatableOptions(TranslationOptions):
    fields = ('full_name',)


@register(VeteranPosition)
class VeteransPositionTranslatableOptions(TranslationOptions):
    fields = ('position', )


@register(Documents)
class DocumentsTranslatableOptions(TranslationOptions):
    fields = ('name', )


@register(Category)
class CategoryTranslatableOptions(TranslationOptions):
    fields = ('name', )


@register(SubCategory)
class SubCategoryTranslatableOptions(TranslationOptions):
    fields = ('name', )


@register(SubSubCategory)
class SubSubCategoryTranslatableOptions(TranslationOptions):
    fields = ('name', )
