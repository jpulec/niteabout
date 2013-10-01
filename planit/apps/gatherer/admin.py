from django.contrib import admin
import requests
import xml.etree.ElementTree as ET
import logging

from planit.apps.gatherer.models import *

logger = logging.getLogger(__name__)

class PlaceAdmin(admin.ModelAdmin):
    fields = ['name', 'pos', 'tags',]
    list_display = ('name', 'pos',)

    filter_horizontal = ('tags',)

class TagAdmin(admin.ModelAdmin):
    fields = ['key', 'value']
    list_display = ('key', 'value',)

admin.site.register(Place, PlaceAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieReview)
