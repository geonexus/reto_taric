__author__ = 'Geon'
from django.conf import settings
from models import Struct
import requests
import logging
logger = logging.getLogger(__name__)


def find_cover_url_by_isbn(isbn):
    """This method recovers the thumbnail image url from googlebooks.
    :return url if everything was ok
    :return None if there is no image or book is not found"""

    response = send_request(isbn)
    search_result = Struct(response.json())
    try:
            return search_result.items[0]['volumeInfo']["imageLinks"]["thumbnail"]

    except AttributeError:
        logger.warn("No book found in googlebooks with ISBN %s", isbn)
    except KeyError:
        logger.warn("Book found in googlebooks with ISBN %s but there is no cover", isbn)


def send_request(query):
    """This method sends a get request to the GoogleBooks API with a given query url."""

    url = settings.GOOGLEBOOKS_API_URL
    response = requests.get(url + query)
    return response
