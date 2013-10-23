from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import AuthenticationForm
from registration.forms import RegistrationForm

import boto.sns

import logging, os
logger = logging.getLogger(__name__)


from niteabout.apps.plan.models import NiteTemplate
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

    def publish_sns(self, activity, who, what):
        conn = boto.sns.SNSConnection(os.environ['AWS_ACCESS_KEY_ID'], os.environ['AWS_SECRET_ACCESS_KEY'])
        message = str(who) + " is looking to get "  + str(activity) + " for " + str(what)
        conn.publish(topic=os.environ['AWS_SNS_ARN'], message=message)

    def get_context_data(self, **kwargs):
        context = super(Plan, self).get_context_data(**kwargs)
        template = NiteTemplate.objects.filter(who=self.request.GET['who'], what=self.request.GET['what']).order_by('?')[:1].get()
        for activity in template.activities:
            pass
            #self.publish_sns(activity.name, self.request.GET['who'], self.request.GET['what'])
        context['template'] = template
        #self.publish_sns(template)
        best_events = []
        weird_events = []
        context['best_events'] = best_events
        context['weird_events'] = weird_events 
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
