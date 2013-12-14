from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

admin.autodiscover()

from niteabout.apps.main.views import Home, About, Contact, Thanks, Profile, RequireProfile, Waiting, Invite

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name="home"),
    url(r'^robots\.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    url(r'^about/$', About.as_view(), name="about"),
    url(r'^contact/$', Contact.as_view(), name='contact'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^profile/$', RequireProfile.as_view(), name="require_profile"),
    url(r'^waiting/$', Waiting.as_view(), name='waiting'),
    url(r'^invite/$', Invite.as_view(), name="invite"),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/profile/$', login_required(Profile.as_view()), name="profile"),
    url(r'^admin/', include(admin.site.urls)),
)
