from django import forms
from django.forms.widgets import HiddenInput, CheckboxSelectMultiple, TextInput

from niteabout.apps.planner.widgets import RangeInput
from niteabout.apps.gatherer.models import StringTag, IntTag, BarSpecial, Genre

PLACE_TYPES = ((tag.value, tag.value.capitalize()) for tag in StringTag.objects.filter(key="amenity").exclude(key='amenity', value__in=['cinema','cafe']))
CUSINE_TYPES = ((tag.value, tag.value.capitalize()) for tag in StringTag.objects.filter(key="cusine"))
BAR_SPECIALS = ((special.deal, special.deal.capitalize()) for special in BarSpecial.objects.all())
CINEMA_GENRES = ((genre.name, genre.name.capitalize()) for genre in Genre.objects.all())

class GetStartedForm(forms.Form):
    location = forms.CharField(max_length=128, required=True, widget=TextInput(attrs={"required":"",
                                                                                      }))
    amenity = forms.ChoiceField(choices=PLACE_TYPES, required=True)
    max_distance = forms.DecimalField(max_digits=3, decimal_places=1, required=True, widget=TextInput(attrs={"required":""}))
    price = forms.IntegerField(required=True, min_value=1, max_value=5, widget=RangeInput(attrs={'max':'5',
                                                                                  'min':'1'}))

class RestaurantForm(forms.Form):
    cusine = forms.MultipleChoiceField(choices=CUSINE_TYPES, widget=CheckboxSelectMultiple(), required=False)
    #volume = forms.IntegerField(required=True, min_value=1, max_value=5, widget=RangeInput(attrs={'max':'5',
    #                                                                              'min':'1'}))

class BarForm(forms.Form):
    specials = forms.MultipleChoiceField(choices=BAR_SPECIALS, widget=CheckboxSelectMultiple(), required=False)
    #volume = forms.IntegerField(required=True, min_value=1, max_value=5, widget=RangeInput(attrs={'max':'5',
    #                                                                              'min':'1'}))
class CafeForm(RestaurantForm):
    pass

class PubForm(BarForm):
    pass

class CinemaForm(forms.Form):
    genres = forms.MultipleChoiceField(choices=CINEMA_GENRES, widget=CheckboxSelectMultiple(), required=True)
