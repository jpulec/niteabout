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

    auth = models.OneToOneField(User, unique=True, blank=True, null=True)
    phone = models.CharField(max_length=24, blank=True)
    location = models.CharField(max_length=256, choices=LOCATION_CHOICES, blank=True)
    interested = models.CharField(max_length=1, choices=INTERESTED_CHOICES, blank=True)
    name = models.CharField(max_length=128, blank=True)
    wings = models.ManyToManyField('UserProfile')

    def __unicode__(self):
        if self.auth:
            return unicode(self.auth)
        return unicode(self.name)

class NiteAbout(models.Model):
    organizer = models.ForeignKey('UserProfile', related_name="organizer")
    attendees = models.ManyToManyField('UserProfile', related_name="attendees", blank=True)
    dt = models.DateTimeField(blank=True, null=True)
    happened = models.BooleanField(default=False)
    filled = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.organizer) + "'s NiteAbout"
