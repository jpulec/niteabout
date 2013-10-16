
window.onload = function() {
	geodjango_geom.map.setCenter(new OpenLayers.LonLat(geodjango_geom.read_wkt(true).geometry.longittude, geodjango_geom.read_wkt(true).geometry.latitude));
};
