from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import PasswordChangeForm

from registration.backends.simple.views import RegistrationView

import stripe

from niteabout.apps.main.forms import ContactForm
from niteabout.apps.events.models import Event

class Home(ListView):
    template_name = "main/home.html"
    context_object_name = "events"
    queryset = Event.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['selected'] = "home"
        return context

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

class Register(RegistrationView):
    def get_success_url(self, request, user):
        return reverse('profile')
