from django.db import models

from niteabout.apps.places.models import Place

class NiteActivity(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

class NiteTimeSpan(models.Model):
    # this will be a timespan in minutes
    timespan = models.IntegerField()

    def __add__(self, other):
        if isinstance(other, NiteTimeSpan):
            return self.timespan + other.timespan
        raise TypeError

    def __unicode__(self):
        return str(self.timespan) + " minutes"

class NiteEvent(models.Model):
    activity = models.ForeignKey('NiteActivity', related_name="activity")
    length = models.ForeignKey('NiteTimeSpan', related_name="length")

    def __unicode__(self):
        return str(self.activity) + " for " + str(self.length)

class NitePlaceEvent(models.Model):
    activity = models.ForeignKey('NiteActivity')
    length = models.ForeignKey('NiteTimeSpan')
    place =  models.ForeignKey(Place, related_name="place")

    def __unicode__(self):
        return str(self.activity) + " at " + str(self.place) + " for " + str(self.length)

class NiteSlot(models.Model):
    time = models.TimeField()
    event = models.ForeignKey('NiteEvent', related_name="event")

    def __unicode__(self):
        return str(self.event) + " at " + self.time.strftime("%I:%M %p")

class NiteTemplate(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    slots = models.ManyToManyField('NiteSlot')

    def __unicode__(self):
        return self.name + ":" + self.description
