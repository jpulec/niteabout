from django import forms
from django.forms.widgets import Textarea, CheckboxSelectMultiple
from django.core.validators import validate_email


import requests
import logging

from niteabout.apps.main.models import UserProfile

logger = logging.getLogger(__name__)

class ContactForm(forms.Form):
    sender = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    subject = forms.CharField(max_length=100,
                              widget=forms.TextInput(attrs={'class':'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control',
                                                           'style':'resize:none'}))

class InviteForm(forms.Form):
    friends = forms.CharField(max_length=256,
                              widget=forms.TextInput(attrs={'class':'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control',
                                                           'style':'resize:none'}))

    def clean_friends(self):
        recipients = self.cleaned_data['friends'].split(',')
        for recipient in recipients:
            validate_email(recipient)
        return recipients

class RequireProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'location', 'interested']
        widgets = {
                'phone': forms.TextInput(attrs={'class':'form-control'}),
                }
        help_texts = {
                'phone': "We're not gonna fuck around with your phone number." +
                         " We only need it in case we need to contact you, or" +
                         " the other group on your Nite needs to get a hold" +
                         " of you. We will NOT use it for anything else."
                }

class AcceptForm(forms.Form):
    name = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={'class':'form-control'}))

class DeclineForm(forms.Form):
    why = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control',
                                                       'style':'resize:none'}))
