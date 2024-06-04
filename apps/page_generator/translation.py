from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(NavLinks)
class NavLinksTranslateOptions(TranslationOptions):
    fields = ('title',)


@register(TextContent)
class textContentTranslateOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(Veteran)
class VeteranTranslateOptions(TranslationOptions):
    fields = ('title', 'full_name', 'rank', 'description',)


@register(Partners)
class PartnersTranslateOptions(TranslationOptions):
    fields = ('name', 'text')


@register(News)
class NewsTranslateOptions(TranslationOptions):
    fields = ('title', 'text')



