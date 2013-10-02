from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.utils.encoding import force_text
from django.http import HttpResponseRedirect
from django.contrib.formtools.wizard.views import NamedUrlSessionWizardView
import inspect

from planit.apps.planner.util import distance_in_miles
from planit.apps.planner.forms import GetStartedForm, RestaurantForm
from planit.apps.gatherer.models import Place, Tag

class GetStarted(FormView):
    template_name = "planner/get_started.html"
    form_class = GetStartedForm
    success_url = "/planit/results/"

    def form_valid(self, form):
        self.request.session['search_query'] = self.request.POST
        return super(GetStarted, self).form_valid(form)

class Results(ListView):
    template_name = "planner/results.html"
    model = Place
    paginate_by = 10
    context_object_name = "places_list"

    def get_queryset(self):
        for item in self.request.session['search_query']:
            print item
        search = self.request.session['search_query']
        threshold = search['max_distance']
        places = Place.objects.filter(tags__value=search['amenity'])
        if 'cusine' in search:
            places = places.filter(tags__value__in=search.getlist('cusine'))
        places = list(places)
        lat, lng = search['location'].split(',')
        for place in list(places):
            if distance_in_miles(place.pos.latitude, place.pos.longitude, lat, lng) > float(threshold):
                places.remove(place)
        return places

    def get_context_data(self, **kwargs):
        context = super(Results, self).get_context_data(**kwargs)
        context['getvars'] = self.request.META['QUERY_STRING']
        context['tags'] = Tag.objects.values('key').distinct()
        return context

FORMS = [("getstarted", GetStartedForm),
         ("restaurant", RestaurantForm)]

FORM_TEMPLATES = {"getstarted": "planner/get_started.html",
                  "restaurant": "planner/restaurant.html"}

#PLACE_TYPES = ((tag.value, tag.value.capitalize()) for tag in Tag.objects.filter(key="amenity"))

def check_restaurant(wizard):
    cleaned_data = wizard.get_cleaned_data_for_step('getstarted') or {'amenity':'none'}
    return cleaned_data['amenity'] == 'restaurant'


planner_conds = {'restaurant':check_restaurant }
#planner_conds = {'restaurant': lambda wizard: wizard.get_cleaned_data_for_step('getstarted').get('amenity', "") == 'restaurant'}
#print [ amenity for amenity in PLACE_TYPES ]
#planner_conds = { amenity[0]:(lambda wizard: wizard.get_cleaned_data_for_step('getstarted').get('amenity', "") == amenity[0]) for amenity in PLACE_TYPES }

class PlannerWizard(NamedUrlSessionWizardView):
    template_name = "planner/get_started.html"

    #def get_template_names(self):
    #    print inspect.getmembers(self.steps)
    #    return [ FORM_TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        for form in form_list:
            for field in form:
                self.request.session['search_query'][field.name] = field
        return HttpResponseRedirect('/planit/results/')



