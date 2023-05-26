from django.contrib import admin
from .models import Entry, Picture


class EntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')


class PictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'entry', 'file', 'created_at')


admin.site.register(Picture, PictureAdmin)
admin.site.register(Entry, EntryAdmin)
