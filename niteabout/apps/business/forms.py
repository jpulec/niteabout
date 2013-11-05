from django import forms
from django.contrib.auth.forms import UserCreationForm

from niteabout.apps.places.models import Place
from niteabout.apps.business.models import Business

class BusinessSignupForm(UserCreationForm):
    name = forms.CharField(max_length=128)
    #place = forms.ModelChoiceField(queryset=Place.objects.all())

    def save(self, commit=True):
        user = super(BusinessSignupForm, self).save(commit=True)
        #business = Business.objects.create(place=self.cleaned_data['place'])
        return user

class BusinessUpdateForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('slug', 'is_active',)
