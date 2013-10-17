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
            ('coed', 'Guys and Girls'),
            )
    WHAT_CHOICES = (
            ('chill', 'A Chill Night'),
            ('date', 'Date'),
            ('laid', 'To Get Laid'),
            ('drunk', 'To Get Drunk'),
            )
    WHERE_CHOICES = (
            ('madison', 'Madison'),
            )

    where = forms.ChoiceField(choices=WHERE_CHOICES, label="Where are you?")
    what = forms.ChoiceField(choices=WHAT_CHOICES, label="What do you need?")
    who = forms.ChoiceField(choices=WHO_CHOICES, label="For whom?")
    when = forms.DateField(label="What day?", widget=forms.TextInput(attrs={'id':'datepicker'}))
