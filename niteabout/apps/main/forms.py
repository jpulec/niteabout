from django import forms
from django.forms.widgets import Textarea

from niteabout.apps.plan.models import NiteWho, NiteWhat

class ContactForm(forms.Form):
    sender = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=Textarea())

class GoForm(forms.Form):
    WHERE_CHOICES = (
            ('madison', 'Madison'),
            )

    where = forms.ChoiceField(choices=WHERE_CHOICES, label="Where are you?")
    what = forms.ModelChoiceField(queryset=NiteWhat.objects.all(), label="What do you need?")
    who = forms.ModelChoiceField(queryset=NiteWho.objects.all(), label="For whom?")
    when = forms.DateField(label="What day?", widget=forms.TextInput(attrs={'id':'datepicker'}))
