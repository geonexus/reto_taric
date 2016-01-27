__author__ = 'Geon'
import requests
import isbn_utils
from django.conf import settings

def search_by_author(author):
    query = "books?q=" + author + "&i=author_name"
    response = send_request(query)
    decoded = isbn_utils.parse_json_to_model(response)
    return decoded
    # print("The ISBN of the most `spoken-about` book with this title is %s" % isbn)
    # print("")
    # print("... and the book is:")
    # print("")
    # print((meta(isbn)))
    # raise Exception("Not implemented yet")

def search_by_ISBN(isbn):
    raise Exception("Not implemented yet")

def search_by_title(title):
    raise Exception("Not implemented yet")

def send_request(query):
    url = settings.ISBNDB_API_URL
    response = requests.get(url + query)
    return response
