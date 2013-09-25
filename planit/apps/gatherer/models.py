from django.db import models
from geoposition.fields import GeopositionField


PLACE_TYPES = (
        ('bar', 'Bar'),
        ('restaurant', 'Restaurant'),
        ('night club', 'Night Club'),
        ('cafe', 'Cafe'),
    )


class Tag(models.Model):
    key = models.CharField(max_length="128")
    value = models.CharField(max_length="256")

    def __unicode__(self):
        return self.key + ":" + self.value

class Place(models.Model):
    tags = models.ManyToManyField('Tag')
    pos = GeopositionField()

    def __unicode__(self):
        return str(self.__dict__)
