from django_rq import job
import requests
import logging, os
import osmread
import datetime

from planit.apps.gatherer.models import Place, Tag

logger = logging.getLogger(__name__)

@job
def parse_openstreetmap(file_name):
    relevant_keys = ["name", "opening_hours", "cusine", "drink", "amenity"]
    relevant_values = ["bar", "pub", "cafe", "restaurant"]
    for entity in osmread.parse_file(file_name):
        if isinstance(entity, osmread.Node):
            if "amenity" in entity.tags:
                if entity.tags['amenity'] in relevant_values and "name" in entity.tags:
                    try:
                        new_place, created = Place.objects.get_or_create(id=entity.id, name=entity.tags['name'], pos=(str(entity.lat) + "," + str(entity.lon)))
                        if new_place.version != entity.version:
                            new_place.version = entity.version
                            new_place.timestamp = datetime.datetime.utcfromtimestamp(entity.timestamp)
                            new_place.save()
                            for k, v in entity.tags.iteritems():
                                if k in relevant_keys or v in relevant_values:
                                    if k != "name":
                                        new_tag, created = Tag.objects.get_or_create(key=k, value=v)
                                        new_place.tags.add(new_tag)
                    except Exception as e:
                        logger.exception(e)
                        return False
    return True

