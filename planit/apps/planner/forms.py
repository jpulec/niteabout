from django import forms
from django.forms.widgets import HiddenInput

from planit.apps.planner.widgets import RangeInput

class GetStartedForm(forms.Form):
    PLACE_TYPES = (
            ('bar', 'Bar'),
            ('restaurant', 'Restaurant')
        )

    location = forms.CharField(max_length=128, widget=HiddenInput())
    location_text = forms.CharField(max_length=128, required=True)
    type = forms.ChoiceField(choices=PLACE_TYPES, required=True)
    price = forms.IntegerField(required=True, min_value=1, max_value=5, widget=RangeInput(attrs={'max':'5',
                                                                                  'min':'1'}))
    max_distance = forms.DecimalField(max_digits=3, decimal_places=1)
