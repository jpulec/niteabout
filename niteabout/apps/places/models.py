from django.db import models
from geoposition.fields import GeopositionField

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
    id = models.IntegerField(primary_key=True)
    tags = models.ManyToManyField('Tag')
    lat = models.FloatField()
    lon = models.FloatField()
    timestamp = models.DateTimeField(null=True)
    version = models.IntegerField(null=True)

    class Meta:
        unique_together = ('id', 'lat', 'lon',)

    def __unicode__(self):
        return str(self.id) + ":" + str(self.lat) + "," + str(self.lon)

class Cuisine(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

class PlaceCategory(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

class Place(models.Model):
    PRICES = (
            (1, "$"),
            (2, "$$"),
            (3, "$$$"),
            (4, "$$$$"),
            (5, "$$$$$"),
            )
    VOLUMES = (
            (1, "Very Quiet"),
            (2, "Quiet"),
            (3, "Moderate"),
            (4, "Loud"),
            (5, "Very Loud"),
            )
    DANCINGS = (
            (1, "It's Bomont"),
            (2, "Stragglers"),
            (3, "A Few Dancers"),
            (4, "People Are on Their Feet"),
            (5, "It's a Mob"),
            )
    ATTIRES = (
            (1, "No Shirt, No Shoes, No Problem"),
            (2, "Sweatpants Allowed"),
            (3, "No Shorts Here"),
            (4, "At Least Wear A Button Down"),
            (5, "Suit Up"),
            )

    osm_place = models.OneToOneField('OSMPlace', blank=True, null=True)
    name = models.CharField(max_length="256")
    pos = GeopositionField()
    categories = models.ManyToManyField('PlaceCategory')
    price = models.PositiveSmallIntegerField(choices=PRICES, blank=True, null=True)
    volume = models.PositiveSmallIntegerField(choices=VOLUMES, blank=True, null=True)
    dancing = models.PositiveSmallIntegerField(choices=DANCINGS, blank=True, null=True)
    attire = models.PositiveSmallIntegerField(choices=ATTIRES, blank=True, null=True)
    cuisines = models.ManyToManyField('Cuisine', blank=True, null=True)

    class Meta:
        unique_together = ('name', 'pos',)

    def __unicode__(self):
        return self.name + ":" + str(self.pos)

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
