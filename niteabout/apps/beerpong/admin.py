from django.contrib import admin

from niteabout.apps.beerpong.models import *

admin.site.register(Team)
admin.site.register(Tournament)
admin.site.register(Round)
admin.site.register(Match)
