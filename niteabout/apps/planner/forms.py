from django import forms
from django.forms.widgets import HiddenInput, CheckboxSelectMultiple, TextInput

from niteabout.apps.planner.widgets import RangeInput
from niteabout.apps.gatherer.models import Tag, BarSpecial, Genre

PLACE_TYPES = ((tag.value, tag.value.capitalize()) for tag in Tag.objects.filter(key="amenity"))
CUSINE_TYPES = ((tag.value, tag.value.capitalize()) for tag in Tag.objects.filter(key="cusine"))
BAR_SPECIALS = ((special.deal, special.deal.capitalize()) for special in BarSpecial.objects.all())
CINEMA_GENRES = ((genre.name, genre.name.capitalize()) for genre in Genre.objects.all())

class GetStartedForm(forms.Form):
    location = forms.CharField(max_length=128, required=True, widget=TextInput(attrs={"required":"",
                                                                                      }))
    amenity = forms.ChoiceField(choices=PLACE_TYPES, required=True)
    max_distance = forms.DecimalField(max_digits=3, decimal_places=1, required=True, widget=TextInput(attrs={"required":""}))
    price = forms.IntegerField(required=True, min_value=1, max_value=5, widget=RangeInput(attrs={'max':'5',
                                                                                  'min':'1'}))
    volume = forms.IntegerField(required=True, min_value=1, max_value=5, widget=RangeInput(attrs={'max':'5',
                                                                                  'min':'1'}))

class RestaurantForm(forms.Form):
    cusine = forms.MultipleChoiceField(choices=CUSINE_TYPES, widget=CheckboxSelectMultiple(), required=False)

class BarForm(forms.Form):
    specials = forms.MultipleChoiceField(choices=BAR_SPECIALS, widget=CheckboxSelectMultiple(), required=False)

class CafeForm(forms.Form):
    pass

class PubForm(forms.Form):
    specials = forms.MultipleChoiceField(choices=BAR_SPECIALS, widget=CheckboxSelectMultiple(), required=False)

class CinemaForm(forms.Form):
    genres = forms.MultipleChoiceField(choices=CINEMA_GENRES, widget=CheckboxSelectMultiple(), required=True)
