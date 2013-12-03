from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from niteabout.apps.beerpong.models import Tournament

class Bracket(DetailView):
    template_name = "beerpong/bracket.html"
    context_object_name = "tournament"
    model = Tournament
