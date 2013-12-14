from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
admin.autodiscover()

from niteabout.apps.main.views import Home, About, Contact, Thanks, Profile, RequireProfile, InviteWings

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name="home"),
    url(r'^robots\.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    url(r'^about/$', About.as_view(), name="about"),
    url(r'^contact/$', Contact.as_view(), name='contact'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^invite/$', InviteWings.as_view(), name="invite_wings"),
    url(r'^profile/$', RequireProfile.as_view(), name="require_profile"),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/profile/$', Profile.as_view(), name="profile"),
    url(r'^admin/', include(admin.site.urls)),
)
