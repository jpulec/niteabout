from django.db import models
from geoposition.fields import GeopositionField

class PlaceType(models.Model):
    PLACE_TYPES = (
            ('bar', 'Bar'),
            ('restaurant', 'Restaurant')
        )

    name = models.CharField(max_length="128", choices=PLACE_TYPES)

    def __unicode__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=128)
    types = models.ManyToManyField('PlaceType')
    pos = GeopositionField()

    def __unicode__(self):
        return str(self.__dict__)

class GooglePlace(models.Model):
    g_id = models.CharField(max_length=256)
    g_rating = models.DecimalField(max_digits=2, decimal_places=1)
    g_price = models.SmallIntegerField()
    reference = models.CharField(max_length=256)
    place = models.OneToOneField('Place', primary_key=True)


    def __unicode__(self):
        return str(self.__dict__)
