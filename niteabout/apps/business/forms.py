from django import forms
from django.contrib.auth.forms import UserCreationForm

from niteabout.apps.places.models import Place
from niteabout.apps.main.models import BusinessProfile

class BusinessSignupForm(UserCreationForm):
    name = forms.CharField(max_length=128)
    place = forms.ModelChoiceField(queryset=Place.objects.all())

    def save(self, commit=True):
        user = super(BusinessSignupForm, self).save(commit=True)
        business_profile = BusinessProfile.objects.create(auth=user, place=self.cleaned_data['place'], name=self.cleaned_data['name'])
        return user
