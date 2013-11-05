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
    max_num = 1

class FeaturesInline(admin.TabularInline):
    model = Feature
    readonly_fields = ('feature_name', 'get_score',)
    extra = 0
    max_num = FeatureName.objects.all().count()

class DealsInline(admin.TabularInline):
    model = Deal
    extra = 1

class FeatureAdmin(admin.ModelAdmin):
    fields = ['feature_name', 'place', 'get_score', 'get_votes']
    readonly_fields = ('get_score', 'get_votes')

    class Meta:
        model = Feature

class PlaceAdmin(OSMGeoAdmin):
    display_wkt = True
    inlines = [
            FeaturesInline,
            HoursInline,
            DealsInline,
            ]
    fields = ['name', 'geom', 'categories', 'cuisines']
    list_display = ('name', 'category_names',)
    filter_horizontal = ('cuisines', 'categories',)

    list_filter = ('categories', 'cuisines',)
    list_related = True

    search_fields = ['name']

    class Meta:
        model = Place

class HourSpanAdmin(admin.ModelAdmin):
    class Meta:
        model = HourSpan

class HoursAdmin(admin.ModelAdmin):
    class Meta:
        model = Hours

class FeatureNameAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories',)
    class Meta:
        model = FeatureName

class FeatureLabelAdmin(admin.ModelAdmin):
    class Meta:
        model = FeatureLabel

admin.site.register(Place, PlaceAdmin)
admin.site.register(Tag)
admin.site.register(Cuisine)
admin.site.register(Hours, HoursAdmin)
admin.site.register(HourSpan, HourSpanAdmin)
admin.site.register(PlaceCategory)
admin.site.register(Deal)
admin.site.register(FeatureName, FeatureNameAdmin)
admin.site.register(FeatureLabel, FeatureLabelAdmin)
#admin.site.register(Feature, FeatureAdmin)
