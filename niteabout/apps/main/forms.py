from django import forms
from django.forms.widgets import Textarea

from niteabout.apps.main.models import UserProfile

class ContactForm(forms.Form):
    sender = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'style':'resize:none'}))

class RequireProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('auth',)
