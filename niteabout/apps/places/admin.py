from django.contrib import admin
from django.contrib.gis.admin.options import OSMGeoAdmin, GeoModelAdmin
from django.contrib.gis.admin.widgets import OpenLayersWidget
from django.conf import settings
import requests
import xml.etree.ElementTree as ET
import logging

from niteabout.apps.places.models import *

logger = logging.getLogger(__name__)

class HoursInline(admin.TabularInline):
    model = Hours
    extra = 7
    max_num = 7

class DealsInline(admin.TabularInline):
    model = Deal
    extra = 1

class PlaceAdmin(OSMGeoAdmin):
    display_wkt = True
    inlines = [
            HoursInline,
            DealsInline,
            ]
    fields = ['name', 'geom', 'categories', 'price', 'volume', 'dancing', 'cuisines', 'attire',]
    list_display = ('name', 'price', 'volume', 'dancing', 'attire', 'category_names',)
    list_editable = ('price', 'volume', 'dancing', 'attire',)
    filter_horizontal = ('cuisines', 'categories',)

    list_filter = ('categories', 'cuisines', 'price', 'volume', 'dancing', 'attire',)
    list_related = True

    search_fields = ['name']

    class Meta:
        model = Place

admin.site.register(Place, PlaceAdmin)
admin.site.register(Tag)
admin.site.register(Cuisine)
admin.site.register(Hours)
admin.site.register(PlaceCategory)
admin.site.register(Deal)
