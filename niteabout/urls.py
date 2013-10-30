from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from niteabout.apps.main.views import Home, About, Contact, Thanks, Profile
from niteabout.apps.plan.views import Plan, Offers, Finalize, Update
from niteabout.apps.places.views import Place
from niteabout.apps.business.views import BusinessView, BusinessPush

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name="home"),
    url(r'^plan/$', Plan.as_view(), name="plan"),
    url(r'^plan/update/$', Update.as_view(), name="update"),
    url(r'^plan/finalize/$', Finalize.as_view(), name="finalize"),
    url(r'^offers/$', Offers.as_view(), name="offers"),
    #url(r'^planit/results/$', Results.as_view(), name="results"),
    #url(r'^planit/(?P<step>.+)/$', planner_wizard, name="planit_step"),
    #url(r'^planit/$', planner_wizard, name="planit"),
    url(r'^place/(?P<pk>\d+)/$', Place.as_view(), name="place"),
    url(r'^about/$', About.as_view(), name="about"),
    url(r'^contact/$', Contact.as_view(), name='contact'),
    url(r'^thanks/$', Thanks.as_view(), name="thanks"),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/profile/$', Profile.as_view(), name="profile"),
    url(r'^business/$', BusinessView.as_view(), name="business"),
    url(r'^business/push/$', BusinessPush.as_view(), name="business_push"),
    url(r'^admin/', include(admin.site.urls)),
)
