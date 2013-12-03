from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import PasswordChangeForm

from organizations.models import OrganizationUser, Organization

from registration.backends.simple.views import RegistrationView

import stripe

from niteabout.apps.places.models import Place
from niteabout.apps.main.forms import ContactForm, GoForm, SignUpForm
from niteabout.apps.plan.models import NitePlan
from niteabout.apps.business.models import Business
from niteabout.apps.main.models import Event

class Home(ListView):
    template_name = "main/home.html"
    context_object_name = "events"
    queryset = Event.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['selected'] = "home"
        return context

class EventView(DetailView, FormView):
    template_name = "main/event.html"
    model = Event
    context_object_name = "event"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        stripe.api_key = "sk_test_mfZIJyxJSBs9pMLDdGs4IG2r"
        token = request.POST['stripeToken']

        try:
            charge = stripe.Charge.create(
                            amount=self.object.cost, # amount in cents, again
                            currency="usd",
                            card=token,
                            description="payinguser@example.com"
                        )
        except stripe.CardError as e:
            pass
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('signup_done')

class SignUp(FormView):
    template_name = "main/signup.html"
    form_class = SignUpForm

    def get_success_url(self, request, user):
        return reverse('signup_done')

class SignUpDone(TemplateView):
    template_name = "main/signup_done.html"

class About(TemplateView):
    template_name = "main/about.html"

    def get_context_data(self, **kwargs):
        context = super(About, self).get_context_data(**kwargs)
        context['selected'] = "about"
        return context

class Contact(FormView):
    template_name = "main/contact.html"
    form_class = ContactForm
    success_url = "/thanks/"

    def get_context_data(self, **kwargs):
        context = super(Contact, self).get_context_data(**kwargs)
        context['selected'] = "contact"
        return context

    def form_valid(self, form):
        recipients = ["jpulec@gmail.com"]
        send_mail(form.cleaned_data['subject'], form.cleaned_data['message'], form.cleaned_data['sender'], recipients)
        return super(Contact, self).form_valid(form)

class Thanks(TemplateView):
    template_name = "main/thanks.html"

class Profile(FormView):
    template_name = "main/profile.html"
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({'user':self.request.user})
        return kwargs

class PastPlans(ListView):
    template_name = "main/pastplans.html"
    context_object_name = "past_plans"

    def get_queryset(self):
        return NitePlan.objects.filter(userprofile=self.request.user.userprofile).order_by('dt')

class Review(ListView):
    template_name = "main/reviewplaces.html"
    context_object_name = "past_places"

    def get_queryset(self):
        past_places = set()
        for plan in NitePlan.objects.filter(userprofile=self.request.user.userprofile):
            for event in plan.events.all():
                for feature in event.place.feature_set.all():
                    if feature.rating.get_rating_for_user(self.request.user) == None:
                        past_places.add(event.place)
        return past_places

class Register(RegistrationView):
    def get_success_url(self, request, user):
        return reverse('profile')
