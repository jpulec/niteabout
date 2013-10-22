from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.core.urlresolvers import reverse

from niteabout.apps.places.models import Place
from niteabout.apps.main.forms import ContactForm, GoForm

class Home(FormView):
    template_name = "main/home.html"
    form_class = GoForm

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

class Place(DetailView):
    model = Place
    template_name = "main/place_view.html"
    context_object_name = "place"

class Thanks(TemplateView):
    template_name = "main/thanks.html"

class Profile(TemplateView):
    template_name = "main/profile.html"
