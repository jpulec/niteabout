from django_rq import job
import requests
import logging, os

from planit.apps.gatherer.models import GooglePlace, PlaceType, Place

logger = logging.getLogger(__name__)


@job
def google_scrape(types):
    location = "43.068302,-89.388352"
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=%s&location=%s&rankby=distance&sensor=false&types=%s" % (os.environ['GOOGLE_API_KEY'], location, types)
    logger.info("Google request url:%s" % url)
    results = None
    try:
        response = requests.get(url).json()
        results = response['results']
        while "next_page_token" in response:
            next_token = response['next_page_token']
            response = requests.get(url + "&pagetoken=%s" % (next_token)).json()
            while response['status'] == "INVALID_REQUEST":
                response = requests.get(url + "&pagetoken=%s" % (next_token)).json()
            results += response['results']
    except requests.ConnectionError as e:
        logger.error("Connection issue:%s" % e)
        return False
    for result in results:
        place, created = Place.objects.get_or_create(name=result['name'], pos=(str(result['geometry']['location']['lat']) + "," + str(result['geometry']['location']['lng'])))
        if not created:
            continue
        else:
            for type in result['types']:
                place_type, created = PlaceType.objects.get_or_create(name=type)
                place.types.add(place_type)
        g_place, created = GooglePlace.objects.get_or_create(place=place, g_id=result['id'], g_rating=result.get('rating', 0.0), g_price=result.get('price', -1), reference=result['reference'])
    return True
