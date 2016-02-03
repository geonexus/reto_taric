__author__ = 'Geon'
import requests
from django.conf import settings
from models import Struct


def search_by(search_type, search_value, page=None):
    """This method search into ISBNdb and recover information about books
    :param search_type Filter to perform the search (author_name, ISBN, publisher_name, title, subject)
    :return Struct with the information about the search."""

    if search_type == "book":
        query = "book/" + search_value
        response = send_request(query)
    elif search_type == "subject":
        if page:
            query = "subjects?q=" + search_value + "&p=" + page
        else:
            query = "subjects?q=" + search_value
        response = send_request(query)
    else:
        if page:
            query = "books?q=" + search_value + "&i=" + search_type + "&p=" + page
        else:
            query = "books?q=" + search_value + "&i=" + search_type
        response = send_request(query)

    # TODO: if seach_type == "subject" (I have to use API v1 because v2 does not support this filter )

    search_result = Struct(response.json())
    return search_result


def send_request(query):
    """This method sends a get request to the ISBNdb API with a given query url."""

    url = settings.ISBNDB_API_URL
    response = requests.get(url + query)
    return response
