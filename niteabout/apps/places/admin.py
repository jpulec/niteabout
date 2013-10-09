from django.contrib import admin
import requests
import xml.etree.ElementTree as ET
import logging

from niteabout.apps.places.models import *

logger = logging.getLogger(__name__)

class PlaceAdmin(admin.ModelAdmin):
    fields = ['name', 'pos', 'tags']
    list_display = ('name', 'pos',)

    filter_horizontal = ('tags',)
    list_filter = ('tag',)
    search_fields = ['name']


class BarSpecialAdmin(admin.ModelAdmin):
    fields = ['bars', 'start_time', 'end_time', 'day', 'deal']
    search_fields = ['bars']
    filter_horizontal = ('bars',)

    #def render_change_form(self, request, context, *args, **kwargs):
    #    specials_tags = StringTag.objects.filter(key='amenity', value__in=['bar','pub'])
    #    context['adminform'].form.fields['bars'].queryset = Bar.objects.filter(string_tags__in=specials_tags)
    #    return super(BarSpecialAdmin, self).render_change_form(request, context, args, kwargs)

admin.site.register(Place, PlaceAdmin)
admin.site.register(Tag)
#admin.site.register(Genre)
#admin.site.register(Movie)
#admin.site.register(MovieReview)
#admin.site.register(MovieShowtime)
admin.site.register(BarSpecial, BarSpecialAdmin)
