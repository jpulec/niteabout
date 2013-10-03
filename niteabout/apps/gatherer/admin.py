from django.contrib import admin
import requests
import xml.etree.ElementTree as ET
import logging

from niteabout.apps.gatherer.models import *

logger = logging.getLogger(__name__)

class PlaceAdmin(admin.ModelAdmin):
    fields = ['name', 'pos', 'string_tags', 'int_tags']
    list_display = ('name', 'pos',)

    filter_horizontal = ('string_tags','int_tags',)
    list_filter = ('string_tags','int_tags',)
    search_fields = ['name']


class StringTagAdmin(admin.ModelAdmin):
    fields = ['key', 'value']
    list_display = ('key', 'value',)
    search_fields = ['key']

class IntTagAdmin(admin.ModelAdmin):
    fields = ['key', 'value']
    list_display = ('key', 'value',)
    search_fields = ['key']

class BarSpecialAdmin(admin.ModelAdmin):
    fields = ['bars', 'start_time', 'end_time', 'day', 'deal']
    search_fields = ['bars']
    filter_horizontal = ('bars',)

    def render_change_form(self, request, context, *args, **kwargs):
        specials_tags = StringTag.objects.filter(key='amenity', value__in=['bar','pub'])
        context['adminform'].form.fields['bars'].queryset = Place.objects.filter(string_tags__in=specials_tags)
        return super(BarSpecialAdmin, self).render_change_form(request, context, args, kwargs)

admin.site.register(Place, PlaceAdmin)
admin.site.register(StringTag, StringTagAdmin)
admin.site.register(IntTag, IntTagAdmin)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieReview)
admin.site.register(MovieShowtime)
admin.site.register(BarSpecial, BarSpecialAdmin)
