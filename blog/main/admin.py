from django.contrib import admin

from main.models import *

# Register your models here.

class MusicianAdmin(admin.ModelAdmin):
    search_fields = ["first_name"]


admin.site.register(Musician, MusicianAdmin)


class AlbumAdmin(admin.ModelAdmin):
    list_filter = ("artist", )

admin.site.register(Album, AlbumAdmin)
