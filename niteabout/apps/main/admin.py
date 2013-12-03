from django.contrib import admin

from niteabout.apps.main.models import *

class UserProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = UserProfile

class EventAdmin(admin.ModelAdmin):
    filter_horizontal  = ('locations',)

    class Meta:
        model = Event

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Event, EventAdmin)
