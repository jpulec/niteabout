from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView
from django.views.generic.list import ListView
from django.core.mail import send_mail
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect

import requests

from registration.backends.simple.views import RegistrationView

from niteabout.apps.main.forms import ContactForm, RequireProfileForm

class Home(TemplateView):
    template_name = "main/home.html"

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

class Profile(TemplateView):
    template_name = "main/profile.html"

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        r = requests.get('https://graph.facebook.com/%s/?fields=picture.type(large)' % self.request.user.social_auth.all()[0].uid)
        data = r.json() 
        context['userpic'] = data['picture']['data']['url']
        return context

class RequireProfile(CreateView):
    template_name = "main/require_profile.html"
    form_class = RequireProfileForm

    def post(self, request, *args, **kwargs):
        profile = request.POST.dict()
        profile.pop('csrfmiddlewaretoken', None)
        request.session['saved_profile'] = profile
        backend = request.session['partial_pipeline']['backend']
        return redirect('social:complete', backend=backend)

class Waiting(TemplateView):
    template_name = "main/waiting.html"

class Invite(TemplateView):
    template_name = "main/invite.html"
