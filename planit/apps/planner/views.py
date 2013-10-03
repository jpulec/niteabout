from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.utils.encoding import force_text
from django.http import HttpResponseRedirect
from django.contrib.formtools.wizard.views import NamedUrlSessionWizardView
from django.contrib.gis.geoip import GeoIP
import logging
import requests

from planit.apps.planner.util import distance_in_miles
from planit.apps.planner.forms import GetStartedForm, RestaurantForm, BarForm, CafeForm, CinemaForm, PubForm
from planit.apps.gatherer.models import Place, Tag

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

    def get_queryset(self):
        search = self.request.session['search_query']
        threshold = search['max_distance']
        places = self.handle(search['amenity'])(search)
        places = list(places)
        lat, lng = geocode(search['location'])
        for place in list(places):
            if distance_in_miles(place.pos.latitude, place.pos.longitude, lat, lng) > float(threshold):
                places.remove(place)
        return places
    
    def handle(self, amenity):
        def handle_amenity(search):
            places = Place.objects.filter(tags__value=search['amenity'])
            if amenity == 'restaurant':
                if search['cusine']:
                    places = places.filter(tags__value__in=search['cusine'])
            elif amenity == 'bar':
                if search['specials']:
                    places = places.filter(barspecial__deal__in=search['specials'])
            elif amenity == 'cinema':
                pass
            return places
        return handle_amenity

    def get_context_data(self, **kwargs):
        context = super(Results, self).get_context_data(**kwargs)
        context['getvars'] = self.request.META['QUERY_STRING']
        context['tags'] = Tag.objects.values('key').distinct()
        return context

FORMS = [("getstarted", GetStartedForm),
         ("restaurant", RestaurantForm),
         ('bar', BarForm),
         ('cafe', CafeForm),
         ('cinema', CinemaForm),
         ('pub', PubForm),]

FORM_TEMPLATES = {"getstarted": "planner/get_started.html",
                  "restaurant": "planner/restaurant.html",
                  "bar":"planner/bar.html",
                  "cafe":"planner/cafe.html"}

PLACE_TYPES = (tag.value for tag in Tag.objects.filter(key="amenity"))

def check_amenity(amenity):
    def check_amenity_func(wizard):
        cleaned_data = wizard.get_cleaned_data_for_step('getstarted') or {'amenity':'none'}
        return cleaned_data['amenity'] == amenity
    return check_amenity_func

planner_conds = { amenity: check_amenity(amenity) for amenity in PLACE_TYPES }

class PlannerWizard(NamedUrlSessionWizardView):
    template_name = "planner/get_started.html"

    #def get_template_names(self):
    #    print inspect.getmembers(self.steps)
    #    return [ FORM_TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        self.request.session['search_query'] = {}
        for form in form_list:
            self.request.session['search_query'].update(form.cleaned_data)
        return HttpResponseRedirect('/planit/results/')

