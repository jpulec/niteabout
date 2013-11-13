#from django_rq import job
import requests
import logging, os
import osmread
from dateutil.parser import parse
import datetime
import feedparser
import xml.etree.ElementTree as ET
from pyqs import task

from django.contrib.gis.geos import Point
from django.db.models.signals import post_save

from niteabout.apps.places.models import Tag, Place, PlaceCategory
from niteabout.apps.places.signals import create_place

logger = logging.getLogger(__name__)


def update(new_place, entity):
    new_place.version = int(entity.version)
    new_place.timestamp = datetime.datetime.utcfromtimestamp(entity.timestamp)
    new_place.save()
    for k, v in entity.tags.iteritems():
        new_tag, created = Tag.objects.get_or_create(key=k, value=v)
        new_place.tags.add(new_tag)

@task(queue='niteabout')
def parse_openstreetmap(file_name):
    post_save.disconnect(receiver=create_place, sender=Place)
    for entity in osmread.parse_file(file_name):
        if isinstance(entity, osmread.Node) and "amenity" in entity.tags and "name" in entity.tags:
            amenity = entity.tags['amenity']
            if amenity in ['bar','pub','restaurant', 'cafe', 'nightclub',]:
                try:
                    new_place, created = Place.objects.get_or_create(osm_id=entity.id, defaults={'name': entity.tags['name'],
                                                                                                 'version': entity.version,
                                                                                                 'geom': Point(entity.lon, entity.lat)})
                    if created:
                        new_category, created = PlaceCategory.objects.get_or_create(name=amenity)
                        new_place.categories.add(new_category)
                        new_place.save()
                        update(new_place, entity)
                    else:
                        if new_place.version < int(entity.version):
                            update(new_place, entity)
                except Exception as e:
                    logger.exception(e)
    post_save.connect(receiver=create_place, sender=Place)
#
#
#@job
#def scrape_rotten_tomatoes_movie():
#    url = "http://api.rottentomatoes/com/api/public/v1.0/movies/"
#
#@job
#def scrape_google_movies(area_code):
#    pass
#

#@task(queue='niteabout-staging')
#def scrape_onconnect(area_code):
#    start_date = datetime.date.today().isoformat()
#    radius = "100"
#    url = "http://data.tmsapi.com/v1/movies/showings?startDate=%s&zip=%s&radius=%s&api_key=%s" % (start_date, area_code, radius, os.environ["ONCONNECT_API_KEY"])
#    logger.info(url)
#    response = requests.get(url)
#    logger.info(response)
#    json = response.json()
#    for movie in json:
#        tms_id = movie['tmsId']
#        title = movie['title']
#        synopsis = movie.get('longDescription', '')
#        if not synopsis:
#            synopsis = movie.get('shortDescription', '')
#        rating = movie.get('ratings', '')
#        if rating:
#            rating[0].get('code', '')
#        genres = movie.get('genres', '')
#        year = movie.get('releaseYear', 0)
#        runtime = movie.get('runTime', 0)
#        new_movie, created = Movie.objects.get_or_create(tms_id=tms_id, defaults={'title':title, 'synopsis':synopsis, 'rating':rating, 'year':year})
#        if created:
#            if genres:
#                for genre in genres:
#                    new_genre, created = Genre.objects.get_or_create(name=genre)
#                    new_movie.genres.add(new_genre)
#                new_movie.save()
#        for showtime in movie['showtimes']:
#            theater_name = showtime['theatre'].get('name', '')
#            theater_id = showtime['theatre']['id']
#            #url = "http://data.tmsapi.com/v1/theatres/%s?api_key=%s" % (theater_id, os.environ['ONCONNECT_API_KEY'])
#            #response = requests.get(url)
#            #logger.info(response)
#            #theater_json = response.json()
#            #lat = theater_json['location']['geoCode']['latitude']
#            #lng = theater_json['location']['geoCode']['longitude']
#            #new_theater, created = Place.objects.get_or_create()
#            time = parse(showtime['dateTime'])
#            new_showtime, created = MovieShowtime.objects.get_or_create(dt=time, movie=new_movie)
#    return True
#
#@job
#def scrape_fandango(area_code):
#    url = "http://www.fandango.com/rss/moviesnearme_%s.rss" % area_code
#    feed = feedparser.parse(url)
#    for theater in feed.entries:
#        theater_name = theater.title
#        logger.indfo(theater_name) 
#        theater_movies = theater.description
#        logger.info(theater_movies)
