from django.views.generic.detail import DetailView

from niteabout.apps.pubgolf.models import PubGolf

class AllScores(DetailView):
    template_name = "pubgolf/all_scores.html"
    model = PubGolf
    context_object_name = "tournament"
