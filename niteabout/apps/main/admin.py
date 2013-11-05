from django.contrib import admin

from niteabout.apps.main.models import *

class UserProfileAdmin(admin.ModelAdmin):
    filter_horizontal = ('past_plans',)
    class Meta:
        model = UserProfile

admin.site.register(UserProfile, UserProfileAdmin)
