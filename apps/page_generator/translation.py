from modeltranslation.translator import register, TranslationOptions

from .models.common_models import PageGenerator
from .models.nav_links import NavLinks
from .models.person import Person
from .models.table import Table, TableDirectionColumn
from .models.text_content import TextContent


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


# @register(Partners)
# class PartnersTranslateOptions(TranslationOptions):
#     fields = ('name', 'text')
#
#
# @register(News)
# class NewsTranslateOptions(TranslationOptions):
#     fields = ('title', 'text')
