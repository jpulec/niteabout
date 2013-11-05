from django.db import models

from niteabout.apps.places.models import Place


class EventCategory(models.Model):
    name = models.CharField(max_length=128)

class Event(models.Model):
    title = models.TextField()
    categories = models.ManyToManyField('EventCategory')
    place = models.ForeignKey(Place)
    datetime = models.DateTimeField()
