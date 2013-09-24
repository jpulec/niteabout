from django.db import models
from geoposition.fields import GeopositionField

class Place(models.Model):
    PLACE_TYPES = (
            ('bar', 'Bar'),
            ('restaurant', 'Restaurant')
        )
    name = models.CharField(max_length=128)
    price = models.SmallIntegerField() 
    type = models.CharField(max_length=128, choices=PLACE_TYPES)
    pos = GeopositionField()

class GooglePlace(Place):
    g_id = models.CharField(max_length=256)
    g_rating = models.DecimalField(max_digits=2, decimal_places=1)
    reference = models.CharField(max_length=256)
