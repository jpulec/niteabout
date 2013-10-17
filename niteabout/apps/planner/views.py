from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.utils.encoding import force_text
from django.http import HttpResponseRedirect
from django.contrib.formtools.wizard.views import NamedUrlSessionWizardView
from django.contrib.gis.geoip import GeoIP
from django.db.models import Q
import logging
import requests

from niteabout.apps.planner.util import distance_in_miles
from niteabout.apps.planner.forms import GetStartedForm, RestaurantForm, BarForm, CafeForm, CinemaForm, PubForm, MoreDetailsForm
from niteabout.apps.places.models import Tag, Place, Deal, PlaceCategory, Cuisine
from niteabout.apps.movies.models import Genre

logger = logging.getLogger(__name__)

class GetStarted(FormView):
    template_name = "planner/get_started.html"
    form_class = GetStartedForm
    success_url = "/planit/results/"

    def form_valid(self, form):
        self.request.session['search_query'] = self.request.POST
        return super(GetStarted, self).form_valid(form)

def geocode(city_state):
    response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false" % city_state)
    logger.info(response)
    json = response.json()
    return json['results'][0]['geometry']['location']['lat'], json['results'][0]['geometry']['location']['lng']

class Results(ListView):
    template_name = "planner/results.html"
    model = Place
    paginate_by = 10
    context_object_name = "places_list"

    def get_context_data(self, **kwargs):
        context = super(Results, self).get_context_data(**kwargs)
        context['selected'] = 'planner'
        return context

    def get_queryset(self):
        search = self.request.session['search_query']
        threshold = search['max_distance']
        places = self.handle_place(search)
        places = list(places)
        lat, lng = geocode(search['location'])
        best_place = None
        best_score = float("inf")
        for place in places:
            if place - search < best_score:
                best_place = place
                best_score = place - search
        return places

    def handle_place(self, search):
        places = Place.objects.filter(categories__name=search['place'])
        if search.get('cuisine', ''):
            places = Place.objects.filter(cusines__name_in=search['cuisine'])
        if search.get('specials', ''):
            places = Place.objects.filter(barspecial__deal__in=search['specials'])
        return places

FORMS = [("Getstarted", GetStartedForm),
         ("MoreDetails", MoreDetailsForm),]
        
       # ("Restaurant", RestaurantForm),
        # ('Bar', BarForm),
        # ('Pub', PubForm),]

FORM_TEMPLATES = {"getstarted": "planner/get_started.html",
                  "restaurant": "planner/restaurant.html",
                  "bar":"planner/bar.html",
                  "cafe":"planner/cafe.html"}

PLACE_TYPES = (c.name for c in PlaceCategory.objects.all())

AMENITY_CORRESPONDING_TAGS = {'restaurant': Cuisine.objects.all(),
                              'bar':Deal.objects.all(),
                              'cinema':Genre.objects.all()}


def check_place(place):
    def check_place_func(wizard):
        cleaned_data = wizard.get_cleaned_data_for_step('Getstarted') or {'place':'none'}
        return cleaned_data['place'] == place
    return check_place_func

planner_conds = { place: check_place(place) for place in PLACE_TYPES }

class PlannerWizard(NamedUrlSessionWizardView):
    template_name = "planner/get_started.html"

    #def get_template_names(self):
    #    print inspect.getmembers(self.steps)
    #    return [ FORM_TEMPLATES[self.steps.current]]

    def get_context_data(self, **kwargs):
        context = super(PlannerWizard, self).get_context_data(**kwargs)
        context['selected'] = 'planner'
        return context

    def done(self, form_list, **kwargs):
        self.request.session['search_query'] = {}
        for form in form_list:
            self.request.session['search_query'].update(form.cleaned_data)
        return HttpResponseRedirect('/planit/results/')

