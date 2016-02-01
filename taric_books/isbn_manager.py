__author__ = 'Geon'
import requests
from django.conf import settings
from models import Struct


def search_by(search_type, search_value, page=None):
    if search_type == "ISBN":
        response = search_by_isbn(search_value)
    else:
        if page:
            query = "books?q=" + search_value + "&i=" + search_type + "&p=" + page
        else:
            query = "books?q=" + search_value + "&i=" + search_type
        response = send_request(query)
    search_result = Struct(response.json())
    return search_result


def search_by_isbn(isbn):
    query = "book/" + isbn
    response = send_request(query)
    return response


def send_request(query):
    url = settings.ISBNDB_API_URL
    response = requests.get(url + query)
    return response
