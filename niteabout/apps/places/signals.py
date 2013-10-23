from django.db.models.signals import m2m_changed, post_save, post_delete
from django.dispatch import receiver
import xml.etree.ElementTree as ET
import requests, logging
import datetime
import os

from decimal import Decimal

from niteabout.apps.places.models import Place, OSMPlace, FeatureName, Feature, Vote
from niteabout.apps.plan.models import NiteTemplate, NiteFeature


logger = logging.getLogger(__name__)


@receiver(post_save, sender=Place)
def create_place(sender, **kwargs):
    created = kwargs.pop('created', False)
    if created:
        instance = kwargs.pop('instance', None)
        payload = """<?xml version='1.0' encoding='utf-8'?><osm><changeset></changeset></osm>"""
        headers = {'content-type': 'application/xml' }
        cs_num = requests.put("http://api.openstreetmap.org/api/0.6/changeset/create", auth=(os.environ['OSM_USERNAME'], os.environ['OSM_PASSWORD']), data=payload, headers=headers)
        logger.info(cs_num.text)
        xml = '<osm><node changeset="' + cs_num.text + '" lat="' + str(instance.geom.y) + '" lon="' + str(instance.geom.x) + '"><tag k="name" v="' + instance.name + '"/></node></osm>'
        response = requests.put("http://api.openstreetmap.org/api/0.6/node/create", data=xml, headers=headers, auth=(os.environ['OSM_USERNAME'], os.environ['OSM_PASSWORD']))
        instance.osm_id = response.text
        instance.save()
        logger.info(response)
        for feature_name in FeatureName.objects.all():
            new_feature = Feature.objects.create(place=place, feature_name=instance)

@receiver(post_save, sender=Vote)
def vote_changed(sender, **kwargs):
    instance = kwargs.pop('instance', None)
    logger.info(instance)
    logger.info(instance.feature.score)
    logger.info(instance.score)
    instance.feature.score = ((instance.feature.score + Decimal(instance.score)) / Decimal(instance.feature.get_votes()))
    instance.feature.save()

@receiver(post_delete, sender=Vote)
def vote_deleted(sender, **kwargs):
    instance = kwargs.pop('instance', None)
    if instance.feature.get_votes() == 0:
        instance.feature.score = 0.0
        instance.feature.save()
    else:
        instance.feature.score = ((instance.feature.score - Decimal(instance.score)) / Decimal(instance.feature.get_votes()))
        instance.feature.save()

@receiver(post_save, sender=FeatureName)
def add_feature(sender, **kwargs):
    created = kwargs.pop('created', False)
    if created:
        instance = kwargs.pop('instance', None)
        logger.info("Creating feature %s for all places..." % instance.name)
        for place in Place.objects.all():
            new_feature = Feature.objects.create(place=place, feature_name=instance)
        logger.info("Creating nitefeature %s for all templates..." % instance.name)
        for template in NiteTemplate.objects.all():
            new_feature = NiteFeature.objects.create(template=template, feature_name=instance)

@receiver(post_save, sender=NiteTemplate)
def add_template(sender, **kwargs):
    created = kwargs.pop('created', False)
    if created:
        instance = kwargs.pop('instance', None)
        for feature_name in FeatureName.objects.all():
            new_feature = NiteFeature.objects.create(template=instance, feature_name=feature_name)


#@receiver(m2m_changed, sender=Place)
def update_osm(sender, **kwargs):
    action = kwargs.pop('action', None)
    instance = kwargs.pop('instance', None)
    if action == "post_add":
        payload = """<?xml version='1.0' encoding='utf-8'?><osm><changeset></changeset></osm>"""
        headers = {'content-type': 'application/xml' }
        cs_num = requests.put("http://api.openstreetmap.org/api/0.6/changeset/create", auth=(), data=payload, headers=headers)
        logger.info(cs_num.text)
        prev_item = requests.get("http://api.openstreetmap.org/api/0.6/node/%s" % instance.id, auth=())
        logger.info("http://api.openstreetmap.org/api/0.6/node/%s" % instance.id)
        logger.info(prev_item)
        tree = ET.fromstring(prev_item.text)
        node = tree.find("node")
        prev_tags = node.findall("tag")
        changed = False
        for tag in instance.string_tags.all():
            if tag.key in ["opening_hours", "cusine"]:
                prev_tag_list = [ prev_tag for prev_tag in prev_tags if prev_tag.get('k') == tag.key]
                for item in prev_tag_list:
                    node.remove(item)
                new_element = ET.Element("tag", attrib={"k":tag.key, "v":tag.value})
                node.insert(0, new_element)
                changed = True
        if changed:
            instance.version = int(node.get('version')) + 1
            node.set('user', "jpulec")
            node.set('timestamp', datetime.datetime.now().isoformat())
            node.set('changeset', cs_num.text)
            response = requests.put("http://api.openstreetmap.org/api/0.6/node/%s" % instance.id, auth=('jpulec', 'Killerjim7'), data=ET.tostring(tree), headers=headers)
            logger.info(response)

