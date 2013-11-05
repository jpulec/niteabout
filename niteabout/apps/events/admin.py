from django.contrib import admin

from niteabout.apps.events.models import *

admin.site.register(Event)
admin.site.register(EventCategory)
