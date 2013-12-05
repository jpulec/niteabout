from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    CHOICES = (
            ('m', 'Men'),
            ('w', 'Women'),
            ('b', 'Both'),
            )

    auth = models.OneToOneField(User, unique=True)
    phone = models.CharField(max_length=24, blank=True)
    location = models.TextField(blank=True)
    interested = models.CharField(max_length=1, choices=CHOICES, blank=True)

    def __unicode__(self):
        return unicode(self.auth)

from niteabout.apps.main import signals
