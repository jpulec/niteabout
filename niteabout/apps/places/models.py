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

class Cuisine(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

class PlaceCategory(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

class Attire(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

class Place(models.Model):
    osm_place = models.OneToOneField('OSMPlace', blank=True, null=True)
    name = models.CharField(max_length="256")
    pos = GeopositionField()
    categories = models.ManyToManyField('PlaceCategory')
    price = models.PositiveSmallIntegerField(blank=True, null=True)
    volume = models.PositiveSmallIntegerField(blank=True, null=True)
    dancing = models.PositiveSmallIntegerField(blank=True, null=True)
    cuisines = models.ManyToManyField('Cuisine', blank=True, null=True)
    attire = models.ForeignKey('Attire', blank=True, null=True)

    class Meta:
        unique_together = ('name', 'pos',)

    def __unicode__(self):
        return self.name + ":" + str(self.pos)

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
        return str(self.place) + " opens at " + str(self.open_time) + " and closes at " + str(self.close_time) + " on " + str(self.day)

class Deal(models.Model):
    place = models.ForeignKey('Place')
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    day = models.IntegerField(max_length=1, choices=DAYS_OF_WEEK, blank=True, null=True)
    deal = models.TextField()

    def __unicode__(self):
        return str(self.place) + " has " + self.deal + " on " + str(self.day) + " starting at " + str(self.start_time) + " until " + str(self.end_time)
