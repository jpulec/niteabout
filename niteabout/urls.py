from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from niteabout.apps.main.views import Home, About, Contact, Place, Thanks, Profile
from niteabout.apps.plan.views import Plan

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name="home"),
    url(r'^plan/$', Plan.as_view(), name="plan"),
    #url(r'^planit/results/$', Results.as_view(), name="results"),
    #url(r'^planit/(?P<step>.+)/$', planner_wizard, name="planit_step"),
    #url(r'^planit/$', planner_wizard, name="planit"),
    url(r'^place/(?P<pk>\d+)/$', Place.as_view(), name="place"),
#    url(r'^django-rq/', include('django_rq.urls')),
#    url(r'^admin/rq/', include('django_rq_dashboard.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Static-y pages
    url(r'^about/$', About.as_view(), name="about"),
    url(r'^contact/$', Contact.as_view(), name='contact'),
    url(r'^thanks/$', Thanks.as_view(), name="thanks"),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/profile/$', Profile.as_view(), name="profile"),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
