from django.views.generic.detail import DetailView

from niteabout.apps.pubgolf.models import Tournament

class AllScores(DetailView):
    template_name = "pubgolf/all_scores.html"
    model = Tournament
    context_object_name = "tournament"
