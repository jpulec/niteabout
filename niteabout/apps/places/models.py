from django.db import models
from geoposition.fields import GeopositionField

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

class Place(models.Model):
    osm_place = models.OneToOneField('OSMPlace', blank=True, null=True)
    name = models.CharField(max_length="256")
    pos = GeopositionField()

    class Meta:
        unique_together = ('name', 'pos',)

    def __unicode__(self):
        return self.name + ":" + str(self.pos)

class PriceMixin(models.Model):
    price = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        abstract = True

class VolumeMixin(models.Model):
    volume = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        abstract = True

class Bar(Place, PriceMixin, VolumeMixin):
    dancing = models.PositiveSmallIntegerField(blank=True, null=True)

class Cuisine(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

class Restaurant(Place, PriceMixin, VolumeMixin):
    cuisines = models.ManyToManyField('Cuisine')

    def cuisine_names(self):
        return ', '.join([c.name for c in self.cuisines.all()])
    cuisine_names.short_description = "Cuisine"

class BarAndRestaurant(Bar, Restaurant):
    pass

class Theater(Place, PriceMixin):
    pass

DAYS_OF_WEEK = (
        (0, "Sunday"),
        (1, "Monday"),
        (2, "Tuesday"),
        (3, "Wednesday"),
        (4, "Thursday"),
        (5, "Friday"),
        (6, "Saturday")
        )

class BarSpecial(models.Model):
    bars = models.ForeignKey('Bar')
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    day = models.IntegerField(max_length=1, default=0, choices=DAYS_OF_WEEK)
    deal = models.TextField()

    def __unicode__(self):
        return str([bar for bar in self.bars.all()]) + " has " + self.deal + " on " + str(self.day) + " starting at " + str(self.start_time) + " until " + str(self.end_time)
