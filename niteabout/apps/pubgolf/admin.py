from django.contrib import admin

from niteabout.apps.pubgolf.models import *

class OrderedHoleInline(admin.TabularInline):
    model = OrderedHole
    ordering = ('order',)
    max_num = 9
    extra = 9

class PubGolfAdmin(admin.ModelAdmin):
    inlines = (OrderedHoleInline,)
    filter_horizontal = ("teams",)

admin.site.register(PubGolf, PubGolfAdmin)
admin.site.register(Team)
admin.site.register(Hole)
admin.site.register(OrderedHole)
admin.site.register(Score)
