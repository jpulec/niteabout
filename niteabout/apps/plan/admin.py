from django.contrib import admin
from niteabout.apps.plan.models import *

class NiteActivityInline(admin.TabularInline):
    model = NiteActivity

class NiteTimeSpanInline(admin.TabularInline):
    model = NiteTimeSpan

class NiteEventInline(admin.TabularInline):
    model = NiteEvent

class NiteSlotInline(admin.TabularInline):
    model = NiteSlot

class NiteEventAdmin(admin.ModelAdmin):
    class Meta:
        model = NiteEvent

class NitePlaceEventAdmin(admin.ModelAdmin):
    class Meta:
        model = NitePlaceEvent

class NiteTimeSpanAdmin(admin.ModelAdmin):
    class Meta:
        model = NiteTimeSpan

class NiteTemplateAdmin(admin.ModelAdmin):
    filter_horizontal = ('slots',)

    class Meta:
        model = NiteTemplate

class NiteSlotAdmin(admin.ModelAdmin):
    class Meta:
        model = NiteSlot

class NiteActivityAdmin(admin.ModelAdmin):
    class Meta:
        model = NiteActivity

admin.site.register(NiteEvent, NiteEventAdmin)
admin.site.register(NitePlaceEvent, NitePlaceEventAdmin)
admin.site.register(NiteTimeSpan, NiteTimeSpanAdmin)
admin.site.register(NiteTemplate, NiteTemplateAdmin)
admin.site.register(NiteSlot, NiteSlotAdmin)
admin.site.register(NiteActivity, NiteActivityAdmin)
