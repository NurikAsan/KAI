from modeltranslation.translator import register, TranslationOptions
from .models.main import BannerWithText
from .models.partners import Partners


@register(Partners)
class PartnersTranslateOptions(TranslationOptions):
    fields = ('name', )


@register(BannerWithText)
class BannerWithTextTranslation(TranslationOptions):
    fields = ('title',)
