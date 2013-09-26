from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from planit.apps.gatherer.models import Place

class Home(TemplateView):
    template_name = "main/home.html"

class Place(DetailView):
    model = Place
    template_name = "main/place_view.html"
    context_object_name = "place"
