from django.db.models.signals import m2m_changed
from django.dispatch import receiver
import xml.etree.ElementTree as ET
import requests, logging
import datetime

from niteabout.apps.gatherer.models import Place


logger = logging.getLogger(__name__)

@receiver(m2m_changed, sender=Place)
def update_osm(sender, **kwargs):
    action = kwargs.pop('action', None)
    instance = kwargs.pop('instance', None)
    if action == "post_add":
        payload = """<?xml version='1.0' encoding='utf-8'?><osm><changeset></changeset></osm>"""
        headers = {'content-type': 'application/xml' }
        cs_num = requests.put("http://api.openstreetmap.org/api/0.6/changeset/create", auth=('jpulec', 'Killerjim7'), data=payload, headers=headers)
        logger.info(cs_num.text)
        prev_item = requests.get("http://api.openstreetmap.org/api/0.6/node/%s" % instance.id, auth=('jpulec', 'Killerjim7'))
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
