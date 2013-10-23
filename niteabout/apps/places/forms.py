from django import forms
from django.forms.models import BaseModelFormSet, modelformset_factory

from niteabout.widgets import FeatureInput
from niteabout.apps.places.models import FeatureName, Vote

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        excludes = ('user', 'feature',)
        widgets = { 'score': FeatureInput() }

class VoteFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super(VoteFormSet, self).__init__(*args, **kwargs)
        self.queryset = Vote.objects.all()

VoteSet = modelformset_factory(Vote, formset=VoteFormSet, form=VoteForm,)
