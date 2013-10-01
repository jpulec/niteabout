from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from planit.apps.main.views import Home, About, Contact, Place, Thanks
from planit.apps.planner.views import GetStarted, Results

urlpatterns = patterns('',
    # Examples:
    url(r'^$', Home.as_view(), name="home"),
    url(r'^planit/$', GetStarted.as_view(), name="planit"),
    url(r'^planit/results/$', Results.as_view(), name="results"),
    url(r'^place/(?P<pk>\d+)/$', Place.as_view(), name="place"),
    url(r'^django-rq/', include('django_rq.urls')),
    url(r'^admin/rq/', include('django_rq_dashboard.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Static-y pages
    url(r'^about/$', About.as_view(), name="about"),
    url(r'^contact/$', Contact.as_view(), name='contact'),
    url(r'^thanks/$', Thanks.as_view(), name="thanks"),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
