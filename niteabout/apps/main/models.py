from django.db import models
from django.contrib.auth.models import User

from niteabout.apps.plan.models import NitePlan

class UserProfile(models.Model):
    auth = models.OneToOneField(User)
    past_plans = models.ManyToManyField(NitePlan, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.auth)
