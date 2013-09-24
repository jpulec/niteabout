from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from planit.apps.planner.forms import GetStartedForm
from planit.apps.gatherer.models import Place

class GetStarted(FormView):
    template_name = "planner/get_started.html"
    form_class = GetStartedForm
    success_url = "/planit/results/"

class Results(ListView):
    template_name = "planner/results.html"
    model = Place
