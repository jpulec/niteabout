from django.contrib.gis.utils import LayerMapping
from niteabout.apps.gatherer.models import Node, node_mapping


def run():
    import pdb; pdb.set_trace()
    lm = LayerMapping(Node, "niteabout/osm/madison_bars.osm", node_mapping, encoding='utf-8', transform=False)
    lm.save(strict=True, verbose=True, progress=True)

if __name__ == "__main__":
    run()
