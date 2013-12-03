from django.conf.urls import patterns, include, url

from niteabout.apps.beerpong.views import Bracket

urlpatterns = patterns('',
    url(r'^beerpong/(?P<pk>\d+)/$', Bracket.as_view(), name="bracket"),
)
