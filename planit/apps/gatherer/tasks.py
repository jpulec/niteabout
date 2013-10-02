from django_rq import job
import requests
import logging, os
import osmread
import dateutil
import datetime
import feedparser
import xml.etree.ElementTree as ET

from planit.apps.gatherer.models import Place, Tag, Movie, MovieShowtime, Genre

logger = logging.getLogger(__name__)

@job
def parse_openstreetmap(file_name):
    relevant_keys = ["name", "opening_hours", "cusine", "drink", "amenity"]
    relevant_values = ["cinema", "bar", "cafe", "pub", "restaurant"]
    for entity in osmread.parse_file(file_name):
        if isinstance(entity, osmread.Node):
            if "amenity" in entity.tags:
                if entity.tags['amenity'] in relevant_values and "name" in entity.tags:
                    try:
                        new_place, created = Place.objects.get_or_create(id=entity.id, name=entity.tags['name'], pos=(str(entity.lat) + "," + str(entity.lon)))
                        if new_place.version < int(entity.version):
                            new_place.version = int(entity.version)
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


@job
def scrape_rotten_tomatoes_movie():
    url = "http://api.rottentomatoes/com/api/public/v1.0/movies/"

@job
def scrape_google_movies(area_code):
    pass

@job
def scrape_onconnect(area_code):
    start_date = datetime.date.today().isoformat()
    radius = "100"
    url = "http://data.tmsapi.com/v1/movies/showings?startDate=%s&zip=%s&radius=%s&api_key=%s" % (start_date, area_code, radius, os.environ["ONCONNECT_API_KEY"])
    response = requests.get(url)
    logger.info(response)
    json = response.json()
    for movie in json:
        id = movie['tmsId']
        title = movie['title']
        synopsis = movie['longDescription']
        rating = movie['ratings'][0].get('code', '')
        genres = movie['genres']
        year = movie['releaseYear']
        runtime = movie['runtime']
        new_movie, created = Movie.objects.get_or_create(id=id, title=title, synopsis=synopsis, rating=rating, year=year)
        if created:
            for genre in genres:
                new_genre, created = Genre.objects.get_or_create(name=genre)
                new_movie.add(new_genre)
            new_movie.save()
        for showtime in movie['showtimes']:
            theater_name = showtime['theatre']['name']
            theater_id = showtime['theatre']['id']
            url = "http://data.tmsapi.com/v1/theatres/%s?api_key=%s" % (theater_id, os.environ['ONCONNECT_API_KEY'])
            response = requests.get(url)
            logger.info(response)
            theater_json = response.json()
            lat = theater_json['location']['geoCode']['latitude']
            lng = theater_json['location']['geoCode']['longitude']
            #new_theater, created = Place.objects.get_or_create()
            time = dateutil.parser.parse(showtime['dateTime'])
            new_showtime, created = MovieShowtime.objects.get_or_create(dt=time, movie=new_movie)
        return True
@job
def scrape_fandango(area_code):
    url = "http://www.fandango.com/rss/moviesnearme_%s.rss" % area_code
    feed = feedparser.parse(url)
    for theater in feed.entries:
        theater_name = theater.title
        logger.indfo(theater_name) 
        theater_movies = theater.description
        logger.info(theater_movies)
