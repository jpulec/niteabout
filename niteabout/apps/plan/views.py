import logging, os, json, math

from django.views.generic import TemplateView, View
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import AuthenticationForm

from registration.forms import RegistrationForm

import boto.sns

from niteabout.apps.plan.models import NiteTemplate, NiteEvent, NitePlan, NiteActivity, NiteActivityName
from niteabout.apps.places.models import Place
from niteabout.apps.business.models import Offer

logger = logging.getLogger(__name__)

class Plan(TemplateView, FormMixin):
    template_name = "plan/plan.html"

    def publish_sns(self, activity, who, what):
        conn = boto.sns.SNSConnection(os.environ['AWS_ACCESS_KEY_ID'], os.environ['AWS_SECRET_ACCESS_KEY'])
        message = str(who) + " is looking to get "  + str(activity) + " for " + str(what)
        conn.publish(topic=os.environ['AWS_SNS_ARN'], message=message)

    def get_context_data(self, **kwargs):
        #TODO: clean this the fuck up
        context = super(Plan, self).get_context_data(**kwargs)
        templates = NiteTemplate.objects.filter(who=self.request.session['query']['who'], what=self.request.session['query']['what']).order_by('?')
        if templates:
            template = templates[0]
            if self.request.user.is_authenticated():
                for activity in template.activities.all():
                    pass
                    #self.publish_sns(activity.name, self.request.GET['who'], self.request.GET['what'])
                context['offers'] = Offer.objects.filter(to_user=self.request.user)
            else:
                context['signup_form'] = RegistrationForm()
                context['signin_form'] = AuthenticationForm()
            context['template'] = template
            best_events = []
            weird_events = []
            nite_plan = NitePlan.objects.create()
            for activity in template.activities.all():
                categories = [cat.name for cat in activity.activity_name.categories.all()]
                places = Place.objects.filter(categories__name__in=categories).order_by('id')
                dists = sorted(map(self.template_sub(template), places), cmp=lambda x,y: cmp(x[1], y[1]))
                for place in dists:
                    if place[0].id not in [event.place.id for event in best_events]:
                        new_nite_event, created = NiteEvent.objects.get_or_create(place=place[0], activity=activity)
                        best_events.append(new_nite_event)
                        nite_plan.events.add(new_nite_event)
                        break
            self.request.session['plan'] = nite_plan
            context['best_events'] = best_events
            context['weird_events'] = weird_events
        return context

    def place_template_diff(self, place, template):
        total = 0
        for feature in place.feature_set.all():
            for nitefeature in template.nitefeature_set.all():
                if nitefeature.feature_name == feature.feature_name:
                    total += pow(feature.get_score() - float(nitefeature.score), 2)
                    break
        return math.sqrt(total)

    def template_sub(self, template):
        def proxy(place):
            return place, self.place_template_diff(place, template)
        return proxy

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
        return super(Plan, self).get(request, *args, **kwargs)

class Offers(ListView):
    template_name = "plan/offers.html"
    context_object_name = "offers"

    def get_queryset(self):
        return Offer.objects.filter(to_user=self.request.user)

class Finalize(TemplateView):
    template_name = "plan/finalize.html"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            self.request.user.userprofile.past_plans.add(self.request.session['plan'])
        return super(Finalize, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Finalize, self).get_context_data(**kwargs)
        return context

class Update(View):

    def post(self, request, *args, **kwargs):
        new_nite_plan = NitePlan.objects.create()
        json_obj = json.loads(self.request.POST['plan'])
        for order, event in enumerate(json_obj):
            new_nite_activity, created = NiteActivity.objects.get_or_create(activity_name=NiteActivityName.objects.get(name__iexact=event['activity']), order=order)
            new_nite_event, created = NiteEvent.objects.get_or_create(activity=new_nite_activity, place=Place.objects.get(id=event['place']))
            new_nite_plan.events.add(new_nite_event)
        self.request.session['plan'] = new_nite_plan
        return HttpResponse('')
