from django_rq import job
import requests
import logging

logger = logging.getLogger(__name__)


@job
def google_scrape():
    location = "-89.0,42.0"
    types = "bar|restaurant"
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=%s&location=%s&rankby=distance&sensor=false&types=%s" % (os.environ['GOOGLE_API_KEY'], location, types)
    logging.info("Google request url:%s" % url)
    try:
        response = requests.get(url).json()
        results = response['results']
        return results
    except requests.ConnectionError as e:
        logging.error("Connection issue:%s" % e)
    return list()
