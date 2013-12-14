from django.contrib import admin

from niteabout.apps.main.models import *

class UserProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = UserProfile

class NiteAboutAdmin(admin.ModelAdmin):
    class Meta:
        model = NiteAbout

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(NiteAbout, NiteAboutAdmin)
