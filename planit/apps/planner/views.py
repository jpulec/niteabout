from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.utils.encoding import force_text
from django.http import HttpResponseRedirect


from planit.apps.planner.util import distance_in_miles
from planit.apps.planner.forms import GetStartedForm
from planit.apps.gatherer.models import Place

class GetStarted(FormView):
    template_name = "planner/get_started.html"
    form_class = GetStartedForm
    success_url = "/planit/results/"


    def get(self, request, *args, **kwargs):
        return super(GetStarted, self).post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(GetStarted, self).get_form_kwargs()
        if self.request.GET:
            kwargs.update({
                'data': self.request.GET})
        return kwargs

    def form_valid(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return force_text(self.success_url + "?" + self.request.META['QUERY_STRING'])

class Results(ListView):
    template_name = "planner/results.html"
    model = Place
    paginate_by = 10

    def get_queryset(self):
        threshold = float(self.request.GET['max_distance'])
        places = list(Place.objects.filter(types__name=self.request.GET['type']))
        lat, lng = self.request.GET['location'].split(',')
        for place in list(places):
            if distance_in_miles(place.pos.latitude, place.pos.longitude, lat, lng) > threshold: 
                places.remove(place)
        return places

    def get_context_data(self, **kwargs):
        context = super(Results, self).get_context_data(**kwargs)
        context['getvars'] = self.request.META['QUERY_STRING']
        return context
