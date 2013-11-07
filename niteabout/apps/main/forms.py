from django import forms
from django.forms.widgets import Textarea

from niteabout.apps.plan.models import NiteWho, NiteWhat

class ContactForm(forms.Form):
    sender = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'style':'resize:none'}))

class GoForm(forms.Form):
    WHERE_CHOICES = (
            ('madison', 'Madison'),
            )

    where = forms.ChoiceField(choices=WHERE_CHOICES, label="Where are you?", widget=forms.Select(attrs={'class':'selectpicker'}))
    what = forms.ModelChoiceField(queryset=NiteWhat.objects.all(), label="What do you need?", widget=forms.Select(attrs={'class':'selectpicker',
                                                                                                                        'data-live-search':'true'}))
    who = forms.ModelChoiceField(queryset=NiteWho.objects.all(), label="For whom?", widget=forms.Select(attrs={'class':'selectpicker'}))
    when = forms.DateField(label="What day?", widget=forms.TextInput(attrs={'class':'form-control datepicker'}))
