from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, FormMixin
from django.views.generic.list import ListView
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.utils.datastructures import MultiValueDictKeyError
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect
from django.conf import settings
from django.utils.http import urlencode

import requests
import cPickle as pickle
import hashlib
import zlib
import logging

from registration.backends.simple.views import RegistrationView

from models import NiteAbout

from forms import ContactForm, RequireProfileForm, InviteForm, AcceptForm, DeclineForm

logger = logging.getLogger(__name__)

class Home(FormView):
    template_name = "main/home.html"
    form_class = InviteForm

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            self.object = self.get_object()
        return super(Home, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            self.object = self.get_object()
        return super(Home, self).post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('invited')

    def form_valid(self, form):
        send_mail(self.request.user.first_name +
                  " Requests That You Be Their Wing",
                  form.cleaned_data['message'] +
                  "\nGo to " + self.generate_url() +
                  " to confirm or deny your attendance" +
                  " and to learn more about NiteAbout.",
                  "NiteAbout",
                  form.cleaned_data['friends'])
        return super(Home, self).form_valid(form)

    def get_object(self):
        if 'niteabout' in self.request.session:
            return self.request.session['niteabout']
        else:
            niteabout, created = NiteAbout.objects.get_or_create(
                    organizer=self.request.user.userprofile,
                    happened=False)
            return niteabout

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            fb_association = self.request.user.social_auth.all()[0]
            context['fb_id'] = fb_association.uid
            context['token'] = fb_association.extra_data['access_token']
            context['niteabout_url'] = self.generate_url()
            context['niteabout'] = self.get_object()
        context['selected'] = "home"
        return context

    def generate_url(self):
        text = zlib.compress(pickle.dumps(self.object,
                                0)
                            ).encode('base64').replace('\n', '')
        m = hashlib.md5(settings.SECRET_KEY + text).hexdigest()[:12]
        url = "http://niteabout.com/invite/?" + urlencode({'m':m, 'text':text})
        logger.info(url)
        return url

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
        recipients = ["james@niteabout.com"]
        send_mail(form.cleaned_data['subject'],
                  form.cleaned_data['message'],
                  form.cleaned_data['sender'],
                  recipients)
        return super(Contact, self).form_valid(form)

class Thanks(TemplateView):
    template_name = "main/thanks.html"

class Profile(TemplateView):
    template_name = "main/profile.html"

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        r = requests.get(
            'https://graph.facebook.com/%s/?fields=picture.type(large)' %
            self.request.user.social_auth.all()[0].uid)
        data = r.json()
        context['userpic'] = data['picture']['data']['url']
        return context

class Invite(DetailView, FormMixin):
    template_name = "main/invite.html"
    model = NiteAbout
    context_object_name = "niteabout"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            # TODO:handle inviting wings that already exist
            raise Http404
        return super(Invite, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = None
        if 'name' in self.request.POST:
            form = AcceptForm(data=self.request.POST)
        elif 'why' in self.request.POST:
            form = DeclineForm(data=self.request.POST)
        else:
            raise Http404
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        if 'name' in self.request.POST:
            return reverse('accept')
        elif 'why' in self.request.POST:
            return reverse('thanks')

    def get_context_data(self, **kwargs):
        context = super(Invite, self).get_context_data(**kwargs)
        context['accept_form'] = AcceptForm()
        context['decline_form'] = DeclineForm()
        return context

    def get_object(self):
        try:
            text = self.request.GET['text']
        except MultiValueDictKeyError as e:
            logger.exception("Invite requires 'text' query parameter")
            raise Http404
        m = hashlib.md5(settings.SECRET_KEY + text).hexdigest()[:12]
        try:
            if m != self.request.GET['m']:
                raise Exception("Bad Hash!")
        except MultiValueDictKeyError as e:
            logger.exception("Invite requires 'm' query parameter")
            raise Http404
        niteabout = pickle.loads(zlib.decompress(text.decode('base64')))
        self.request.session['niteabout'] = niteabout
        return niteabout

class RequireProfile(FormView):
    template_name = "main/require_profile.html"
    form_class = RequireProfileForm

    def form_valid(self, form):
        profile = self.request.POST.dict()
        profile.pop('csrfmiddlewaretoken', None)
        self.request.session['saved_profile'] = profile
        backend = self.request.session['partial_pipeline']['backend']
        return redirect('social:complete', backend=backend)

class Invited(TemplateView):
    template_name = "main/invited.html"

class Accept(TemplateView):
    template_name = "main/accept.html"

class Decline(TemplateView):
    template_name = "main/decline.html"

class FAQ(TemplateView):
    template_name = "main/faq.html"
