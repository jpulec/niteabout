from django.core.management.base import BaseCommand, CommandError

from niteabout.apps.business.models import Offer

import datetime

class Command(BaseCommand):
    help = 'Expires offers that are too old'

    def handle(self, *args, **options):
        Offer.objects.filter(expiration__lte=datetime.datetime.now()).delete()
