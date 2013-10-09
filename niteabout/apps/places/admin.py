from django.contrib import admin
import requests
import xml.etree.ElementTree as ET
import logging

from niteabout.apps.places.models import *

logger = logging.getLogger(__name__)

class PlaceAdmin(admin.ModelAdmin):
    fields = ['name', 'pos']
    list_display = ('name', 'pos',)

    search_fields = ['name']

    class Meta:
        model = Place
        abstract = True

class BarAdmin(PlaceAdmin):
    fields = PlaceAdmin.fields + ['price', 'volume', 'dancing']
    list_display = PlaceAdmin.list_display + ('price', 'volume', 'dancing',)
    list_editable = ('price','volume','dancing',)

    class Meta:
        model = Bar

class RestaurantAdmin(PlaceAdmin):
    fields = PlaceAdmin.fields + ['price', 'volume','cuisines',]
    list_display = PlaceAdmin.list_display + ('price', 'volume', 'cuisine_names',)
    list_editable = ('price','volume',)
    filter_horizontal = ('cuisines',)

    class Meta:
        model = Restaurant

class BarSpecialAdmin(admin.ModelAdmin):
    fields = ['bars', 'start_time', 'end_time', 'day', 'deal']
    search_fields = ['bars']
    filter_horizontal = ('bars',)

    #def render_change_form(self, request, context, *args, **kwargs):
    #    specials_tags = StringTag.objects.filter(key='amenity', value__in=['bar','pub'])
    #    context['adminform'].form.fields['bars'].queryset = Bar.objects.filter(string_tags__in=specials_tags)
    #    return super(BarSpecialAdmin, self).render_change_form(request, context, args, kwargs)

admin.site.register(OSMPlace)
admin.site.register(Bar, BarAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Tag)
admin.site.register(Cuisine)
#admin.site.register(Genre)
#admin.site.register(Movie)
#admin.site.register(MovieReview)
#admin.site.register(MovieShowtime)
admin.site.register(BarSpecial)
