__author__ = 'Geon'
import requests
import isbn_utils
from django.conf import settings

def search_by(filter, value ):
    query = "books?q=" + value + "&i=" + filter
    response = send_request(query)
    list_of_books = isbn_utils.get_list_of_books(response)
    return list_of_books

def search_by_ISBN(isbn):
    raise Exception("Not implemented yet")

def search_by_title(title):
    raise Exception("Not implemented yet")

def send_request(query):
    url = settings.ISBNDB_API_URL
    response = requests.get(url + query)
    return response
