from django.contrib import admin
import requests
import xml.etree.ElementTree as ET
import logging

from niteabout.apps.places.models import *

logger = logging.getLogger(__name__)

class HoursInline(admin.TabularInline):
    model = Hours

class PlaceAdmin(admin.ModelAdmin):
    fields = ['name', 'pos', 'categories', 'price', 'volume', 'dancing', 'cuisines', 'attire',]
    list_display = ('name', 'price', 'volume', 'dancing', 'attire', 'category_names',)
    list_editable = ('price', 'volume', 'dancing', 'attire',)
    filter_horizontal = ('cuisines', 'categories',)

    list_filter = ('categories', 'cuisines', 'price', 'attire', 'volume', 'dancing',)
    list_related = True
    inlines = [
            HoursInline,
            ]

    search_fields = ['name']

    class Meta:
        model = Place

admin.site.register(OSMPlace)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Tag)
admin.site.register(Cuisine)
admin.site.register(Hours)
admin.site.register(PlaceCategory)
admin.site.register(Attire)
admin.site.register(Deal)
