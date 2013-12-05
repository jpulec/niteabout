from django.contrib import admin

from niteabout.apps.main.models import *

class UserProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = UserProfile

admin.site.register(UserProfile, UserProfileAdmin)
