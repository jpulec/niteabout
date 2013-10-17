from django import forms
from django.forms.widgets import Textarea

class ContactForm(forms.Form):
    sender = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=Textarea())

class GoForm(forms.Form):
    WHO_CHOICES = (
            ('me', 'Me'),
            ('partner', 'My Partner and I'),
            ('guys', "Bro's Night"),
            ('girls', "Girl's Night"),
            )
    WHAT_CHOICES = (
            ('chill', 'A Chill Night'),
            ('date', 'Date'),
            ('laid', 'To Get Laid'),
            )


    what = forms.ChoiceField(choices=WHAT_CHOICES)
    who = forms.ChoiceField(choices=WHO_CHOICES)
    when = forms.DateField(widget=forms.TextInput(attrs={'id':'datepicker'}))
