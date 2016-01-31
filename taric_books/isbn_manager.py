__author__ = 'Geon'
import requests
import isbn_utils
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
    search_result = Struct(response.json())
    return search_result


def search_by_title(title):
    raise Exception("Not implemented yet")


def search_by_author(author, page=None):
    if page:
        response = search_by("author_name", author, page=page)
    else:
        response = search_by("author_name", author)
    search_result = Struct(response.json())
    # list_of_books = isbn_utils.get_list_of_books(response)
    # for book in list_of_books:
    #     mybook = Struct(book)
    #     print mybook.isbn13 +mybook.title_latin
    return search_result


def search_by_publisher(publisher):
    raise Exception("Not implemented yet")


def search_by_topic(topic):
    raise Exception("Not implemented yet")


def send_request(query):
    url = settings.ISBNDB_API_URL
    response = requests.get(url + query)
    return response
