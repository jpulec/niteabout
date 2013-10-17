from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import logging
logger = logging.getLogger(__name__)


from niteabout.apps.plan.models import NiteTemplate, NitePlaceEvent
from niteabout.apps.places.models import Place

NITE_TEMPLATES = {'me':
                    {'date':'Classic Date'},
                }

class Plan(TemplateView):
    template_name = "plan/plan.html"

    def get_context_data(self, **kwargs):
        context = super(Plan, self).get_context_data(**kwargs)
        template_name = NITE_TEMPLATES[self.request.GET['who']][self.request.GET['what']]
        template = NiteTemplate.objects.get(name__iexact=template_name)
        context['timespans'] = (slot.time for slot in sorted(template.slots.all(), key=lambda slot: slot.time))
        best_events = []
        weird_events = []
        for slot in sorted(template.slots.all(), key=lambda slot: slot.time):
            if slot.event.activity.name == "Drinks":
                place = Place.objects.filter(categories__name__iexact="bar").order_by('?')[:1].get()
                new_nite_place_event, created = NitePlaceEvent.objects.get_or_create(place=place, activity=slot.event.activity, length=slot.event.length)
                best_events.append(new_nite_place_event)
                weird_events.append(new_nite_place_event)
            elif slot.event.activity.name == "Dinner":
                place = Place.objects.filter(categories__name__iexact="restaurant").order_by('?')[:1].get()
                new_nite_place_event, created = NitePlaceEvent.objects.get_or_create(place=place, activity=slot.event.activity, length=slot.event.length)
                best_events.append(new_nite_place_event)
                weird_events.append(new_nite_place_event)
        context['best_events'] = best_events
        context['weird_events'] = weird_events
        return context

    def get(self, request, *args, **kwargs):
        if not request.GET:
            #no query parameters, what the hell are they doing here?
            return HttpResponseRedirect(reverse("home"))
        return super(Plan, self).get(request, *args, **kwargs)
