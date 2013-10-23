from django import forms
from django.contrib.auth.forms import UserCreationForm

from niteabout.apps.places.models import Place

PLACE_CHOICES = ( (x.name, x.name) for x in Place.objects.all())

class BusinessSignupForm(UserCreationForm):
    name = forms.CharField(max_length=128)
    place = forms.ChoiceField(choices=PLACE_CHOICES)
