from modeltranslation.translator import translator, TranslationOptions
from page.models import Page

class PageTranslationOptions(TranslationOptions):
    fields = ('content',)

translator.register(Page, PageTranslationOptions)
