from django.contrib import admin
from niteabout.apps.plan.models import *

class NiteActivityInline(admin.TabularInline):
    model = NiteActivity

class NiteFeatureInline(admin.TabularInline):
    model = NiteFeature
    extra = 0
    max_num = FeatureName.objects.all().count()

class NiteTemplateAdmin(admin.ModelAdmin):
    inlines = [
            NiteFeatureInline,
            ]
    filter_horizontal = ('activities', 'who', 'what',)
    class Meta:
        model = NiteTemplate

class NiteActivityNameAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories',)

    class Meta:
        model = NiteActivityName

class NiteActivityAdmin(admin.ModelAdmin):
    class Meta:
        model = NiteActivity

class NiteWhoAdmin(admin.ModelAdmin):
    class Meta:
        model = NiteWho

class NiteWhatAdmin(admin.ModelAdmin):
    class Meta:
        model = NiteWhat

class NiteFeatureAdmin(admin.ModelAdmin):
    class Meta:
        model = NiteFeature

class NitePlanAdmin(admin.ModelAdmin):
    filter_horizontal = ('events',)
    class Meta:
        model = NitePlan

admin.site.register(NiteTemplate, NiteTemplateAdmin)
admin.site.register(NiteActivity, NiteActivityAdmin)
admin.site.register(NiteActivityName, NiteActivityNameAdmin)
#admin.site.register(NiteFeature, NiteFeatureAdmin)
admin.site.register(NiteWho, NiteWhoAdmin)
admin.site.register(NitePlan, NitePlanAdmin)
admin.site.register(NiteWhat, NiteWhatAdmin)
