from django import forms

from niteabout.widgets import FeatureInput
from niteabout.apps.places.models import FeatureName

import logging

logger = logging.getLogger(__name__)

class FeatureForm(forms.Form):
    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance', None)
        super(FeatureForm, self).__init__(*args, **kwargs)
        for feature_name in FeatureName.objects.filter(categories__in=instance.categories.all()):
            self.fields['%s' % feature_name.name] = forms.IntegerField(widget=FeatureInput(attrs={'class':'col-lg-6'}))
