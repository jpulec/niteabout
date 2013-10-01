from django import forms
from django.forms.widgets import HiddenInput, CheckboxSelectMultiple

from planit.apps.planner.widgets import RangeInput
from planit.apps.gatherer.models import Tag

PLACE_TYPES = ((tag.value, tag.value.capitalize()) for tag in Tag.objects.filter(key="amenity"))
CUSINE_TYPES = ((tag.value, tag.value.capitalize()) for tag in Tag.objects.filter(key="cusine"))

class GetStartedForm(forms.Form):
    location = forms.CharField(max_length=128, required=True, widget=HiddenInput())
    location_text = forms.CharField(max_length=128, required=True)
    amenity = forms.ChoiceField(choices=PLACE_TYPES, required=True)
    price = forms.IntegerField(required=True, min_value=1, max_value=5, widget=RangeInput(attrs={'max':'5',
                                                                                  'min':'1'}))
    max_distance = forms.DecimalField(max_digits=3, decimal_places=1)
    cusine = forms.MultipleChoiceField(choices=CUSINE_TYPES, required=False, widget=CheckboxSelectMultiple())
