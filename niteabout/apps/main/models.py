from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    INTERESTED_CHOICES = (
            ('m', 'Men'),
            ('w', 'Women'),
            ('b', 'Both'),
            )

    LOCATION_CHOICES = (
            ('madison', 'Madison'),
            )

    auth = models.OneToOneField(User, unique=True)
    phone = models.CharField(max_length=24, blank=True)
    location = models.CharField(max_length=256, choices=LOCATION_CHOICES)
    interested = models.CharField(max_length=1, choices=INTERESTED_CHOICES, blank=True)
    wings = models.ManyToManyField('UserProfile')

    def __unicode__(self):
        return unicode(self.auth)

from niteabout.apps.main import signals
