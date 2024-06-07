from modeltranslation.translator import register, TranslationOptions
from .models.news import News
from .models.advertisements import Advertisements


@register(News)
class NewsTranslateOptions(TranslationOptions):
    fields = ('title', 'text')


@register(Advertisements)
class NewsTranslateOptions(TranslationOptions):
    fields = ('title', 'text')
