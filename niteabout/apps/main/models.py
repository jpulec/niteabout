from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    auth = models.OneToOneField(User)

    def __unicode__(self):
        return unicode(self.auth)

from niteabout.apps.main import signals
