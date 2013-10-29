from django.db import models
from django.contrib.auth.models import User

from niteabout.apps.main.models import BusinessProfile

import datetime

class Offer(models.Model):
    owner = models.ForeignKey(BusinessProfile)
    text = models.TextField()
    to_user = models.ForeignKey(User)
    expiration = models.DateTimeField(default=datetime.datetime.now()+datetime.timedelta(minutes=30))
