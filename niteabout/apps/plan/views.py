from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import AuthenticationForm
from registration.forms import RegistrationForm

import boto.sns

import logging, os
logger = logging.getLogger(__name__)


from niteabout.apps.plan.models import NiteTemplate, NitePlaceEvent
from niteabout.apps.places.models import Place

NITE_TEMPLATES = {'me':
                    {'date':'Classic Date'},
                }

class Row(object):
    def __init__(self, best, time, weird):
        self.best = best
        self.time = time
        self.weird = weird

class Plan(TemplateView, FormMixin):
    template_name = "plan/plan.html"

    def publish_sns(self, template):
        conn = boto.sns.SNSConnection(os.environ['AWS_ACCESS_KEY_ID'], os.environ['AWS_SECRET_ACCESS_KEY'])
        for slot in template.slots.all():
            if slot.event.activity.name == "Drinks":
                message = self.request.user.username + " is looking for drinks"
                conn.publish(topic=os.environ['AWS_SNS_ARN'], message=message)
            elif slot.event.activity.name == "Dinner":
                message = self.request.user.username + " is looking for dinner"
                conn.publish(topic=os.environ['AWS_SNS_ARN'], message=message)

    def get_context_data(self, **kwargs):
        context = super(Plan, self).get_context_data(**kwargs)
        template_name = NITE_TEMPLATES[self.request.GET['who']][self.request.GET['what']]
        template = NiteTemplate.objects.get(name__iexact=template_name)
        context['timespans'] = (slot.time for slot in sorted(template.slots.all(), key=lambda slot: slot.time))
        timespans = context['timespans']
        #self.publish_sns(template)
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
        context['rows'] = [Row(best_event, timespan, weird_event) for best_event, timespan, weird_event in zip(best_events, timespans, weird_events) ]
        context['signup_form'] = RegistrationForm()
        context['signin_form'] = AuthenticationForm()
        return context

    def post(self, request, *args, **kwargs):
        form_class = None
        if 'signup' in request.POST:
            form_class = RegistrationForm
        elif 'signin' in request.POST:
            form_class = AuthenticationForm
        form = self.get_form(form_class)

    def get_success_url(self):
        if 'signup' in self.request.POST:
            pass
        elif 'signin' in self.request.POST:
            return HttpResponse(reverse('finalize'))

    def get(self, request, *args, **kwargs):
        if not request.GET:
            #no query parameters, what the hell are they doing here?
            return HttpResponseRedirect(reverse("home"))
        return super(Plan, self).get(request, *args, **kwargs)
