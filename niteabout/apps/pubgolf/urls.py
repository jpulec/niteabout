from django.conf.urls import patterns, include, url

from niteabout.apps.pubgolf.views import AllScores

urlpatterns = patterns('',
    url(r'^pubgolf/(?P<pk>\d+)/$', AllScores.as_view(), name="all_scores"),
)
