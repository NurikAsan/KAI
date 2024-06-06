from modeltranslation.translator import register, TranslationOptions
from .models.main import BannerWithText
from .models.partners import Partners


@register(Partners)
class PartnersTranslateOptions(TranslationOptions):
    fields = ('name', )


# @register(News)
# class NewsTranslateOptions(TranslationOptions):
#     fields = ('title', 'text')

@register(BannerWithText)
class BannerWithTextTranslation(TranslationOptions):
    fields = ('title',)
