import logging

from django.db.models.signals import post_save
from django.contrib.auth.models import User

from niteabout.apps.main.models import UserProfile

logger = logging.getLogger(__name__)

@receiver(post_save, sender=User)
def create_user(sender, **kwargs):
    created = kwargs.pop('created', False)
    if created:
        instance = kwargs.pop('instance', None)
        new_profile = UserProfile.objects.create(auth=instance)
