from django.contrib import admin

from planit.apps.gatherer.models import *

class PlaceAdmin(admin.ModelAdmin):
    fields = ['name', 'pos', 'tags',]
    list_display = ('name', 'loudness', 'opening_hours', 'amenity', )

    #def save_modal(self, request, obj, form, change):

class TagAdmin(admin.ModelAdmin):
    fields = ['key', 'value']
    list_display = ('key',)

admin.site.register(Place, PlaceAdmin)
admin.site.register(Tag, TagAdmin)
