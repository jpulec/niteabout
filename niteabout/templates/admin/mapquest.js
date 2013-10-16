{% extends "gis/admin/openlayers.js" %}
{% block base_layer %}
new OpenLayers.Layer.XYZ(
		"Imagery",
		[
		"http://otile1.mqcdn.com/tiles/1.0.0/map/${z}/${x}/${y}.png",
		"http://otile2.mqcdn.com/tiles/1.0.0/map/${z}/${x}/${y}.png",
		"http://otile3.mqcdn.com/tiles/1.0.0/map/${z}/${x}/${y}.png",
		"http://otile4.mqcdn.com/tiles/1.0.0/map/${z}/${x}/${y}.png"
		],
		{
			attribution: "Tiles Courtesy of <a href='http://open.mapquest.co.uk/' target='_blank'>MapQuest</a>. Portions Courtesy NASA/JPL-Caltech and U.S. Depart. of Agriculture, Farm Service Agency. <img src='http://developer.mapquest.com/content/osm/mq_logo.png' border='0'>",
    transitionEffect: "resize"
		}
		)
{% endblock %}
