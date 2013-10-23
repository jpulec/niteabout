from django.db import models
from django.contrib.auth.models import User

from niteabout.apps.plan.models import NitePlan
from niteabout.apps.places.models import Place

class UserProfile(models.Model):
    auth = models.OneToOneField(User)
    past_plans = models.ManyToManyField(NitePlan)

    def __unicode__(self):
        return str(self.auth)

class BusinessProfile(models.Model):
    auth = models.OneToOneField(User)
    place = models.OneToOneField(Place)
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return str(self.auth)
