import datetime

from django.db import models
from django.contrib.auth.models import User

from organizations.models import Organization

from niteabout.apps.places.models import Place

class Business(Organization):
    place = models.OneToOneField(Place)

class Offer(models.Model):
    owner = models.ForeignKey(Organization)
    text = models.TextField()
    to_user = models.ForeignKey(User)
    expiration = models.DateTimeField(default=datetime.datetime.now()+datetime.timedelta(minutes=30))
