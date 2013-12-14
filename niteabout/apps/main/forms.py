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

class InviteWingsForm(forms.Form):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(InviteWingsForm, self).__init__(*args, **kwargs)
        r = requests.get("https://graph.facebook.com/%s/?fields=friends&access_token=%s" % (user.social_auth.all()[0].uid, user.social_auth.all()[0].extra_data['access_token'])).json()
        for friend in r['friends']:
            self.fields["id_%s" % friend] = forms.CharField(max_length=64)
