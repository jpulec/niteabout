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
    id = models.IntegerField(primary_key=True)
    tags = models.ManyToManyField('Tag', related_name="tags")
    name = models.CharField(max_length="256")
    pos = GeopositionField()
    timestamp = models.DateTimeField(null=True)
    version = models.IntegerField(null=True)


    def loudness(self):
        return self.tags.get(key="loudness").value

    def opening_hours(self):
        return self.tags.get(key="opening_hours").value

    def amenity(self):
        return self.tags.filter(key="amenity").values_list('value', flat=True)

    def get_tags(self):
        return self.tags.all()

    def __unicode__(self):
        return self.name + ":" + str(self.pos)
