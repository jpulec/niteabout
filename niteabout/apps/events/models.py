from django.db import models

from niteabout.apps.main.models import UserProfile

class GooglePlace(models.Model):
    g_id = models.CharField(max_length=256)
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name

class OrderedPlace(models.Model):
    place = models.ForeignKey('GooglePlace')
    event = models.ForeignKey('Event')
    order = models.IntegerField()

    def __unicode__(self):
        return "Stop:" + unicode(self.order) + " at " + unicode(self.place) + " for " + unicode(self.event)

class Event(models.Model):
    active = models.BooleanField()
    dt = models.DateTimeField()
    name = models.CharField(max_length=256)
    description = models.TextField()
    cost = models.IntegerField()  #this should be in cents

    def __unicode__(self):
        return self.name + " at " + unicode(self.dt)
