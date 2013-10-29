from django.db import models
from django.contrib.gis.db import models as geomodels
from django.contrib.auth.models import User

from djangoratings.fields import RatingField

from decimal import Decimal

import logging

logger = logging.getLogger(__name__)

class Tag(models.Model):
    key = models.CharField(max_length="128")
    value = models.CharField(max_length="256")

    def __unicode__(self):
        return self.key + ":" + self.value

    class Meta:
        unique_together = ('key', 'value',)

class OSMPlace(models.Model):
    osm_id = models.BigIntegerField(blank=True, null=True)
    tags = models.ManyToManyField('Tag', null=True, blank=True)
    timestamp = models.DateTimeField(null=True)
    version = models.IntegerField(null=True)

    class Meta:
        abstract= True

    def __unicode__(self):
        return str(self.osm_id)



class Cuisine(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

class PlaceCategory(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

class FeatureName(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

class Feature(models.Model):
    feature_name = models.ForeignKey('FeatureName')
    place = models.ForeignKey('Place')
    rating = RatingField(range=range(-5,6), can_change_vote=True, weight=10)

    class Meta:
        unique_together = ('feature_name', 'place',)

    def get_score(self):
        return self.rating.get_rating()

    def get_votes(self):
        return self.rating.votes
    
    def __unicode__(self):
        return unicode(self.place) + ":" + unicode(self.feature_name) + ":" + unicode(self.rating)

class Place(OSMPlace):
    name = models.CharField(max_length=256)
    geom = geomodels.PointField()
    categories = models.ManyToManyField('PlaceCategory')
    cuisines = models.ManyToManyField('Cuisine', blank=True, null=True)
    objects = geomodels.GeoManager() 

    def __unicode__(self):
        return str(self.name)

    def __sub__(self, other):
        if isinstance(other, Place):
            return 0
        else:
            raise TypeError

    def category_names(self):
        return ', '.join([c.name for c in self.categories.all()])
    category_names.short_description = "Categories"

class HourSpan(models.Model):
    open = models.TimeField()
    close = models.TimeField()

    def __unicode__(self):
        return unicode(self.open) + "-" + unicode(self.close)

class Hours(models.Model):
    place = models.ForeignKey('Place')
    sunday = models.ForeignKey('HourSpan', related_name="sunday_hours", blank=True, null=True)
    monday = models.ForeignKey('HourSpan', related_name="monday_hours", blank=True, null=True)
    tuesday = models.ForeignKey('HourSpan', related_name="tuesday_hours", blank=True, null=True)
    wednessday = models.ForeignKey('HourSpan', related_name="wednesday_hours", blank=True, null=True)
    thursday = models.ForeignKey('HourSpan', related_name="thursday_hours", blank=True, null=True)
    friday = models.ForeignKey('HourSpan', related_name="friday_hours", blank=True, null=True)
    saturday = models.ForeignKey('HourSpan', related_name="saturday_hours", blank=True, null=True)

    def __unicode__(self):
        return unicode(self.place) + " hours"

DAYS_OF_WEEK = (
        ('Su', 'Sunday'),
        ('M', 'Monday'),
        ('Tu', 'Tuesday'),
        ('W', 'Wednesday'),
        ('Th', 'Thursday'),
        ('F', 'Friday'),
        ('Sa', 'Saturday'),
        )

class Deal(models.Model):
    place = models.ForeignKey('Place')
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    day = models.IntegerField(max_length=1, choices=DAYS_OF_WEEK, blank=True, null=True)
    deal = models.TextField()

    def __unicode__(self):
        return str(self.place) + " has " + self.deal + " on " + self.get_day_display() + " starting at " + str(self.start_time) + " until " + str(self.end_time)

from niteabout.apps.places import signals
