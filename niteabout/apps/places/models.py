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
    name = models.CharField(max_length=256)
    pos = GeopositionField()
    timestamp = models.DateTimeField(null=True)
    version = models.IntegerField(null=True)

    def __unicode__(self):
        return self.name + str(self.pos)

class Place(models.Model):
    osm_place = models.OneToOneField('OSMPlace', blank=True, null=True)
    name = models.CharField(max_length="256")
    pos = GeopositionField()

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name + ":" + str(self.pos)

class PriceMixin(models.Model):
    price = models.PositiveSmallIntegerField()

    class Meta:
        abstract = True

class VolumeMixin(models.Model):
    volume = models.PositiveSmallIntegerField()

    class Meta:
        abstract = True

class Bar(Place, PriceMixin, VolumeMixin):
    dancing = models.PositiveSmallIntegerField()

class Cusine(models.Model):
    name = models.CharField(max_length=128)

class Restaurant(Place, PriceMixin, VolumeMixin):
    cusine = models.ForeignKey('Cusine')

class BarAndRestaurant(Bar, Restaurant):
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
