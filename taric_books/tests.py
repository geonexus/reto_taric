"""
This file contains all tests related to taric_books project.

To tests this module you should execute
"python manage.py test taric_books" from root directory of the project reto_taric

"""
__author__ = 'Geon'

from django.test import TestCase
from django.conf import settings
from mock import patch
import json
import isbn_manager
from reto_taric.constants import UNIT_TEST_RESOURCES_FOLDER, FILE_NAME_AUTHOR_SEARCH_RESPONSE

""" Class to test the interaction with isbndb
"""

class isbn_client_tests(TestCase):
    # This method will be used by the mock to replace requests.get

    def setUp(self):

        self.author = "Eduardo Mendoza"
        self.filter_author = "author_name"

    def mocked_requests_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data

        query_author = "books?q=" + "Eduardo Mendoza" + "&i=" + "author_name"
        query_isbn = "book?q=" + "9788408105626"

        if args[0] == settings.ISBNDB_API_URL + query_author:
            return MockResponse(json.loads(open(UNIT_TEST_RESOURCES_FOLDER +
                                                FILE_NAME_AUTHOR_SEARCH_RESPONSE).read()), 200)
        elif args[0] == settings.ISBNDB_API_URL + query_author:
            return MockResponse({"data": "value2"}, 200)

        return MockResponse({}, 404)

    @patch('requests.get', side_effect=mocked_requests_get)
    def test_search_client_by_author(self, mock_get):
        """Tests if method gets a list of books."""

        # with patch.object(isbn_manager.requests, 'get', return_value=response) as mock_method:

        response = isbn_manager.search_by(self.filter_author, self.author)
        self.assertEqual(response, json.loads(open(UNIT_TEST_RESOURCES_FOLDER +
                                                   FILE_NAME_AUTHOR_SEARCH_RESPONSE).read())["data"])
