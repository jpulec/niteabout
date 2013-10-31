from django import forms

from niteabout.widgets import FeatureInput
from niteabout.apps.places.models import FeatureName

import logging

logger = logging.getLogger(__name__)

class FeatureForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(FeatureForm, self).__init__(*args, **kwargs)
        for feature_name in FeatureName.objects.all():
            self.fields['%s' % feature_name.name] = forms.IntegerField(widget=FeatureInput())
