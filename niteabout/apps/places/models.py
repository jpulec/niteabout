from django.db import models
from django.contrib.gis.db import models as geomodels
from geoposition.fields import GeopositionField

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

class Place(OSMPlace):
    name = models.CharField(max_length=256)
    geom = geomodels.PointField()
    categories = models.ManyToManyField('PlaceCategory')
    price = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    volume = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    dancing = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    attire = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    cuisines = models.ManyToManyField('Cuisine', blank=True, null=True)
    objects = geomodels.GeoManager() 

    def __unicode__(self):
        return str(self.name) + ":" + str(self.geom)

    def __sub__(self, other):
        if isinstance(other, Place):
            return pow(
                    pow(self.price - other.price, 2) + 
                    pow(self.volume - other.volume, 2) + 
                    pow(self.dancing - other.dancing, 2) +
                    pow(self.attire - other.attire, 2),
                    0.5)
        elif isinstance(other, dict):
            total = 0
            for k,v in other.iteritems():
                try:
                    total += pow(getattr(self, k) - v, 2)
                except Exception as e:
                    logger.exception(e)
            return pow(total, 0.5)
        else:
            raise TypeError

    def category_names(self):
        return ', '.join([c.name for c in self.categories.all()])
    category_names.short_description = "Categories"

DAYS_OF_WEEK = (
        (0, "Sunday"),
        (1, "Monday"),
        (2, "Tuesday"),
        (3, "Wednesday"),
        (4, "Thursday"),
        (5, "Friday"),
        (6, "Saturday")
        )

class Hours(models.Model):
    place = models.ForeignKey('Place')
    day = models.IntegerField(choices=DAYS_OF_WEEK, unique=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __unicode__(self):
        return str(self.place) + " opens at " + str(self.start_time) + " and closes at " + str(self.end_time) + " on " + self.get_day_display()

class Deal(models.Model):
    place = models.ForeignKey('Place')
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    day = models.IntegerField(max_length=1, choices=DAYS_OF_WEEK, blank=True, null=True)
    deal = models.TextField()

    def __unicode__(self):
        return str(self.place) + " has " + self.deal + " on " + self.get_day_display() + " starting at " + str(self.start_time) + " until " + str(self.end_time)

from niteabout.apps.places import signals
