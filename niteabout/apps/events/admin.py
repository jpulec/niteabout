from django.contrib import admin

from niteabout.apps.events.models import *

class OrderedPlaceInline(admin.TabularInline):
    model = OrderedPlace
    extra = 2

class EventAdmin(admin.ModelAdmin):
    inlines = (OrderedPlaceInline,)

admin.site.register(Event, EventAdmin)
admin.site.register(GooglePlace)
admin.site.register(OrderedPlace)
