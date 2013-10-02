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
    list_filter = ('tags',)
    search_fields = ['name']


class TagAdmin(admin.ModelAdmin):
    fields = ['key', 'value']
    list_display = ('key', 'value',)
    search_fields = ['key']

class BarSpecialAdmin(admin.ModelAdmin):
    fields = ['bar', 'start_time', 'end_time', 'day', 'deal']
    search_fields = ['bar']

    def render_change_form(self, request, context, *args, **kwargs):
        specials_tags = Tag.objects.filter(key='amenity', value__in=['bar','pub'])
        context['adminform'].form.fields['bar'].queryset = Place.objects.filter(tags__in=specials_tags)
        return super(BarSpecialAdmin, self).render_change_form(request, context, args, kwargs)

admin.site.register(Place, PlaceAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieReview)
admin.site.register(BarSpecial, BarSpecialAdmin)
