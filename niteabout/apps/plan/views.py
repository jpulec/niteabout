from django.views.generic import TemplateView, View
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import AuthenticationForm
from registration.forms import RegistrationForm

import boto.sns

import logging, os, json
logger = logging.getLogger(__name__)


from niteabout.apps.plan.models import NiteTemplate, NiteEvent, NitePlan, NiteActivity, NiteActivityName
from niteabout.apps.places.models import Place
from niteabout.apps.business.models import Offer

class Plan(TemplateView, FormMixin):
    template_name = "plan/plan.html"

    def publish_sns(self, activity, who, what):
        conn = boto.sns.SNSConnection(os.environ['AWS_ACCESS_KEY_ID'], os.environ['AWS_SECRET_ACCESS_KEY'])
        message = str(who) + " is looking to get "  + str(activity) + " for " + str(what)
        conn.publish(topic=os.environ['AWS_SNS_ARN'], message=message)

    def get_context_data(self, **kwargs):
        context = super(Plan, self).get_context_data(**kwargs)
        template = NiteTemplate.objects.filter(who=self.request.GET['who'], what=self.request.GET['what']).order_by('?')[:1].get()
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
            logger.info(activity)
            categories = [cat.name for cat in activity.activity_name.categories.all()]
            place = Place.objects.filter(categories__name__in=categories).order_by('?')[:1].get()
            new_nite_event, created = NiteEvent.objects.get_or_create(place=place, activity=activity)
            best_events.append(new_nite_event)
            nite_plan.events.add(new_nite_event)
        self.request.session['plan'] = nite_plan
        context['best_events'] = best_events
        context['weird_events'] = weird_events
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
        context['final_events'] = self.request.session['plan'].events.order_by('activity')
        return context

class Update(View):

    def post(self, request, *args, **kwargs):
        new_nite_plan = NitePlan.objects.create()
        json_obj = json.loads(self.request.POST['plan'])
        for order, event in enumerate(json_obj):
            new_nite_activity, created = NiteActivity.objects.get_or_create(activity_name=NiteActivityName.objects.get(name=event['activity']), order=order)
            new_nite_event, created = NiteEvent.objects.get_or_create(activity=new_nite_activity, place=Place.objects.get(id=event['place']))
            new_nite_plan.events.add(new_nite_event)
        self.request.session['plan'] = new_nite_plan
        return HttpResponse('')
