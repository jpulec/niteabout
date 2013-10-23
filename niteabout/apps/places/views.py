from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin, FormView, ProcessFormView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from niteabout.apps.places.models import Place
from niteabout.apps.places.forms import VoteSet, VoteForm

class Place(DetailView, FormView):
    model = Place
    template_name = "place/place_view.html"
    context_object_name = "place"
    form_class = VoteSet

    #def get_context_data(self, **kwargs):
    #    context = super(Place, self).get_context_data(**kwargs)
    #    if self.request.POST:
    #        context['formset'] = VoteSet(self.request.POST)
    #    else:
    #        context['formset'] = VoteSet()
    #    return context

    def get(self, request, *args, **kwargs):
        formset_class = self.get_form_class()
        formset = self.get_form(formset_class)
        self.object = self.get_object()
        context = self.get_context_data(object=self.object, formset=formset)
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse('profile')

    #def form_valid(self, form):
    #    for feature_name, feature_value in form.cleaned_data.iteritems():
    #        vote = Vote.objects.create(user=self.request.user, score=feature_value, feature=Feature.objects.get(feature_name=feature_name, place=self.object))

