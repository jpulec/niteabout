from django import forms
from django.forms.widgets import CheckboxSelectMultiple

from niteabout.apps.places.models import FeatureName
from niteabout.apps.plan.models import NiteActivityName
from niteabout.widgets import FeatureInput

class RefineForm(forms.Form):
    num_places = forms.IntegerField(min_value=1, max_value=10)
    activities = forms.ModelMultipleChoiceField(queryset=NiteActivityName.objects.all(), widget=CheckboxSelectMultiple())

    def __init__(self, *args, **kwargs):
        super(RefineForm, self).__init__(*args, **kwargs)
        for feature_name in FeatureName.objects.all():
            self.fields['%s' % feature_name.name] = forms.IntegerField(widget=FeatureInput(attrs={'class':'col-lg-6'}))
