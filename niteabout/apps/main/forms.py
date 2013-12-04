from django import forms
from django.forms.widgets import Textarea

class ContactForm(forms.Form):
    sender = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'style':'resize:none'}))
