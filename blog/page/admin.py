from django.contrib import admin

from page.models import *

class PageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Page, PageAdmin)
