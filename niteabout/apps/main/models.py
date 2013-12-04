from django.db import models
from django.contrib.auth.models import User

from niteabout.apps.plan.models import NitePlan

from niteabout.apps.places.models import Place

class OrderedPlace(models.Model):
    place = models.ForeignKey(Place)
    event = models.ForeignKey('Event')
    order = models.IntegerField()

class Event(models.Model):
    active = models.BooleanField()
    dt = models.DateTimeField()
    name = models.CharField(max_length=256)
    description = models.TextField()
    cost = models.IntegerField()
    locations = models.ManyToManyField(Place, related_name="ordered_places", through="OrderedPlace")
    attendees = models.ManyToManyField(User, blank=True)

    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    auth = models.OneToOneField(User)

    def __unicode__(self):
        return unicode(self.auth)

from niteabout.apps.main import signals
