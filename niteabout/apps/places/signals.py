import xml.etree.ElementTree as ET
import requests, logging
import datetime
import os

from django.db.models.signals import m2m_changed, post_save, post_delete, pre_save
from django.dispatch import receiver
from django.conf import settings

from niteabout.apps.places.models import Place, OSMPlace, FeatureName, Feature, PlaceCategory
from niteabout.apps.plan.models import NiteTemplate, NiteFeature

logger = logging.getLogger(__name__)

osm_api_url = "http://api.openstreetmap.org/api/0.6/"


def get_changeset_id():
    changeset_id = None
    if not 'osm_changeset_id' in settings:
        changeset_root = ET.Element('osm')
        changeset_node = ET.SubElement(changeset_root, "changeset")
        changeset_created_by = ET.SubElement(changeset_node, "tag", attrib={'k':"created_by", 'v':'NiteAbout'})
        changeset_id = settings['osm_changeset_id'] = requests.put(osm_api_url + "changeset/create", auth=(os.environ['OSM_USERNAME'], os.environ['OSM_PASSWORD']), data=ET.tostring(changeset_root, encoding='UTF-8'), headers=headers).text
    else:
        changeset_id = settings['osm_changeset_id']
        response = requests.get(osm_api_url + "changeset/%s" % changeset_id)
        tree = ET.fromstring(response.text)
        changeset = tree.find('changeset')
        if not changeset.attrib['open'] == 'true':
            changeset_root = ET.Element('osm')
            changeset_node = ET.SubElement(changeset_root, "changeset")
            changeset_created_by = ET.SubElement(changeset_node, "tag", attrib={'k':"created_by", 'v':'NiteAbout'})
            changeset_id = settings['osm_changeset_id'] = requests.put(osm_api_url + "changeset/create", auth=(os.environ['OSM_USERNAME'], os.environ['OSM_PASSWORD']), data=ET.tostring(changeset_root, encoding='UTF-8'), headers=headers).text
    return changeset_id

#@receiver(pre_save, sender=Place)
def check_for_updates(sender, **kwargs):
    created = False #kwargs.pop('created', False)
    instance = kwargs.pop('instance', None)
    response = requests.get(osm_api_url + "node/%s" % instance.id, auth=(os.environ['OSM_USERNAME'], os.environ['OSM_PASSWORD']))
    if response.status_code == 200:
        tree = ET.fromstring(response.text)
        node = tree.find("node")
        prev_tags = node.findall("tag")
        if instance.version < int(node.attrib['version']):
            # OSM has newer version
            instance.version = int(node.attrib['version'])
            instance.timestamp = datetime.datetime.utcfromtimestamp(node.attrib['timestamp'])
            for tag in prev_tags:
                new_tag, created = Tag.objects.get_or_create(key=tag.attrib['k'], value=tag.attrib['v'])
                new_place.tags.add(new_tag)


#@receiver(post_save, sender=Place)
def create_place(sender, **kwargs):
    created = False #kwargs.pop('created', False)
    changeset_id = get_changeset_id()
    if created:
        instance = kwargs.pop('instance', None)
        payload = """<?xml version='1.0' encoding='utf-8'?><osm><changeset></changeset></osm>"""
        headers = {'content-type': 'application/xml' }
        # Grab changeset or open new one
        changeset_id = get_changeset_id()
        root = ET.Element('osm')
        node = ET.SubElement(root, "node", attrib={'changeset':changeset_id,
                                                   'lat': unicode(instance.geom.y),
                                                   'lon': unicode(instance.geom.x)})
        # set all tags
        for tag in instance.tags:
            tag_node = ET.SubElement(node, 'tag', attrib={'k':tag.key, 'v':tag.value})
        response = requests.put(osm_api_url + "node/create", data=root, headers=headers, auth=(os.environ['OSM_USERNAME'], os.environ['OSM_PASSWORD']))
        instance.osm_id = response.text
        instance.save()
        logger.info(response)
        for feature_name in FeatureName.objects.all():
            new_feature = Feature.objects.create(place=instance, feature_name=feature_name)
    else:
        response = requests.get(osm_api_url + "node/%s" % instance.id, auth=(os.environ['OSM_USERNAME'], os.environ['OSM_PASSWORD']))
        if response.status_code == 200:
            tree = ET.fromstring(response.text)
            node = tree.find("node")
            prev_tags = node.findall("tag")
            if instance.version < int(node.attrib['version']):
                # OSM has newer version
                update(instance, node)
                for tag in prev_tags:
                    new_tag, created = Tag.objects.get_or_create(key=tag.attrib['k'], value=tag.attrib['v'])
        root = ET.Element('osm')
        node = ET.SubElement(root, "node", attrib={'changeset':changeset_id,
                                                   'lat': unicode(instance.geom.y),
                                                   'lon': unicode(instance.geom.x)})
        # set all tags
        for tag in instance.tags:
            tag_node = ET.SubElement(node, 'tag', attrib={'k':tag.key, 'v':tag.value})
        response = requests.put(osm_api_url + "node/create", data=root, headers=headers, auth=(os.environ['OSM_USERNAME'], os.environ['OSM_PASSWORD']))


#@receiver(pre_save, sender=FeatureName)
def feature_pre_save(sender, instance, **kwargs):
    if instance.pk:
        instance._old_m2m = set(list(instance.categories.values_list('pk', flat=True)))
    else:
        instance._old_m2m = set(list())

@receiver(m2m_changed, sender=FeatureName.categories.through)
def feature_changed(sender, **kwargs):
    instance = kwargs.pop('instance', None)
    action = kwargs.pop('action', None)
    if action == "post_add":
        pk_set = kwargs.pop('pk_set', None)
        logger.info("Creating feature %s for all places with categories:%s" % (instance.name, unicode(pk_set)))
        for place in Place.objects.filter(categories__pk__in=pk_set):
            new_feature, created  = Feature.objects.get_or_create(place=place, feature_name=instance)
        logger.info("Creating nitefeature %s for all templates..." % instance.name)
        for template in NiteTemplate.objects.all():
            new_feature, created = NiteFeature.objects.get_or_create(template=template, feature_name=instance)
    #elif action == "post_clear":
    #    logger.info("Removing feature %s for places not in categories:%s" % (instance.name, instance._old_m2m))
    #    Feature.objects.filter(place__categories__pk__in=instance._old_m2m).delete()

@receiver(post_save, sender=NiteTemplate)
def add_template(sender, **kwargs):
    created = kwargs.pop('created', False)
    if created:
        instance = kwargs.pop('instance', None)
        for feature_name in FeatureName.objects.all():
            new_feature = NiteFeature.objects.create(template=instance, feature_name=feature_name)

#@receiver(pre_save, sender=Place)
def place_pre_save(sender, instance, **kwargs):
    if instance.pk:
        instance._old_m2m = set(list(instance.categories.values_list('pk', flat=True)))
    else:
        instance._old_m2m = set(list())

@receiver(m2m_changed, sender=Place.categories.through)
def place_update_categories(sender, **kwargs):
    instance = kwargs.pop('instance', None)
    action = kwargs.pop('action', None)
    if action == "post_add":
        pk_set = kwargs.pop('pk_set', None)
        logger.info("Creating features:%s for %s" % (unicode(pk_set), instance.name))
        for feature_name in FeatureName.objects.filter(categories__pk__in=pk_set):
            new_feature, created  = Feature.objects.get_or_create(place=instance, feature_name=feature_name)
    elif action == "post_clear":
        #TODO: get this working
        pass
        #logger.info("Removing feature:%s for %s" % (instance._old_m2m, instance.name))
        #Feature.objects.filter(place=instance, feature_name__categories__pk__in=instance._old_m2m).delete()

@receiver(m2m_changed, sender=Place.cuisines.through)
def update_cusines(sender, **kwargs):
    action = kwargs.pop('action', None)
    instance = kwargs.pop('instance', None)
    model = kwargs.pop('model', None)
    if action == "post_add":
        pk_set = kwargs.pop('pk_set', None)
        new_tag, created = Tag.objects.get_or_create(key="cuisine", value=";".join([cuisine.name for cuisine in Cuisine.objects.filter(pk__in=pk_set)]))
        instance.tags.add(new_tag)
    #    changed = False
    #    for tag in instance.string_tags.all():
    #        if tag.key in ["opening_hours", "cusine"]:
    #            prev_tag_list = [ prev_tag for prev_tag in prev_tags if prev_tag.get('k') == tag.key]
    #            for item in prev_tag_list:
    #                node.remove(item)
    #            new_element = ET.Element("tag", attrib={"k":tag.key, "v":tag.value})
    #            node.insert(0, new_element)
    #            changed = True
    #    if changed:
    #        instance.version = int(node.get('version')) + 1
    #        node.set('user', "jpulec")
    #        node.set('timestamp', datetime.datetime.now().isoformat())
    #        node.set('changeset', cs_num.text)
    #        response = requests.put("http://api.openstreetmap.org/api/0.6/node/%s" % instance.id, auth=(os.environ['OSM_USERNAME'], os.environ['OSM_PASSWORD']), data=ET.tostring(tree), headers=headers)
    #        logger.info(response)
