from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin, FormView, ProcessFormView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from djangoratings.models import Vote

from niteabout.apps.places.models import Place, Feature
from niteabout.apps.places.forms import FeatureForm

import logging

logger = logging.getLogger(__name__)

class Place(DetailView, FormView):
    model = Place
    template_name = "place/place_view.html"
    context_object_name = "place"
    form_class = FeatureForm

    #def get_context_data(self, **kwargs):
    #    context = super(Place, self).get_context_data(**kwargs)
    #    if self.request.POST:
    #        context['formset'] = VoteSet(self.request.POST)
    #    else:
    #        context['formset'] = VoteSet()
    #    return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(Place, self).post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def get_initial(self):
        initial = super(Place, self).get_initial()
        if self.request.user.is_authenticated():
            for feature in Feature.objects.filter(place=self.object):
                prev_vote = feature.rating.get_rating_for_user(user=self.request.user)
                if prev_vote:
                    initial[feature.feature_name.name] = prev_vote
        return initial

    def get_success_url(self):
        return reverse('profile')

    def form_valid(self, form):
        for feature_name, feature_value in form.cleaned_data.iteritems():
            feature, created = Feature.objects.get_or_create(feature_name__name=feature_name, place=self.object)
            feature.rating.add(score=feature_value, user=self.request.user, ip_address=self.request.META['REMOTE_ADDR'])
        return HttpResponseRedirect(self.get_success_url())
