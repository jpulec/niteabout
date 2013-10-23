from django.contrib import admin
from niteabout.apps.plan.models import *

class NiteActivityInline(admin.TabularInline):
    model = NiteActivity

class NiteTemplateAdmin(admin.ModelAdmin):
    filter_horizontal = ('activities', 'who', 'what',)
    class Meta:
        model = NiteTemplate

class NiteActivityAdmin(admin.ModelAdmin):
    class Meta:
        model = NiteActivity

class NiteWhoAdmin(admin.ModelAdmin):
    class Meta:
        model = NiteWho

class NiteWhatAdmin(admin.ModelAdmin):
    class Meta:
        model = NiteWhat

admin.site.register(NiteTemplate, NiteTemplateAdmin)
admin.site.register(NiteActivity, NiteActivityAdmin)
admin.site.register(NiteWho, NiteWhoAdmin)
admin.site.register(NiteWhat, NiteWhatAdmin)
