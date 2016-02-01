"""
This file contains all tests related to taric_books project.

To tests this module you should execute
"python manage.py test taric_books" from root directory of the project reto_taric

"""
__author__ = 'Geon'

from django.test import TestCase
from django.test import Client
from unittest import SkipTest
from django.conf import settings
from mock import patch
import json
import isbn_manager
import gbooks_covers
from reto_taric.constants import UNIT_TEST_RESOURCES_FOLDER, FILE_NAME_AUTHOR_SEARCH_RESPONSE, \
    FILE_NAME_ISBN_SEARCH_RESPONSE, FILE_NAME_COVER_SEARCH_RESPONSE, FILE_NAME_COVER_SEARCH_NO_IMAGE_RESPONSE,\
    FILE_NAME_COVER_SEARCH_NO_BOOK_RESPONSE

""" Class to test the interaction with isbndb
"""


class isbn_client_tests(TestCase):
    # This method will be used by the mock to replace requests.get

    def setUp(self):

        self.author = "Eduardo Mendoza"
        self.filter_author = "author_name"
        self.filter_isbn = "ISBN"

        self.title = "Rina de gatos"
        self.ISBN = "9788408105626"
        self.ISBN_for_cover = "9788432291395"
        self.ISBN_no_cover = "9781582346816"
        self.ISBN_no_book_cover = "0000000000000"

    def mocked_requests_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data

        query_author = "books?q=" + "Eduardo Mendoza" + "&i=" + "author_name"
        query_isbn = "book/" + "9788408105626"
        ISBN_with_cover = "9788432291395"
        ISBN_without_cover = "9781582346816"
        ISBN_no_book_cover = "0000000000000"

        if args[0] == settings.ISBNDB_API_URL + query_author:
            return MockResponse(json.loads(open(UNIT_TEST_RESOURCES_FOLDER +
                                                FILE_NAME_AUTHOR_SEARCH_RESPONSE).read()), 200)
        elif args[0] == settings.ISBNDB_API_URL + query_isbn:
            return MockResponse(json.loads(open(UNIT_TEST_RESOURCES_FOLDER +
                                                FILE_NAME_ISBN_SEARCH_RESPONSE).read()), 200)
        elif args[0] == settings.GOOGLEBOOKS_API_URL + ISBN_with_cover:
            return MockResponse(json.loads(open(UNIT_TEST_RESOURCES_FOLDER +
                                                FILE_NAME_COVER_SEARCH_RESPONSE).read()), 200)
        elif args[0] == settings.GOOGLEBOOKS_API_URL + ISBN_without_cover:
            return MockResponse(json.loads(open(UNIT_TEST_RESOURCES_FOLDER +
                                                FILE_NAME_COVER_SEARCH_NO_IMAGE_RESPONSE).read()), 200)
        elif args[0] == settings.GOOGLEBOOKS_API_URL + ISBN_no_book_cover:
            return MockResponse(json.loads(open(UNIT_TEST_RESOURCES_FOLDER +
                                                FILE_NAME_COVER_SEARCH_NO_BOOK_RESPONSE).read()), 200)

        return MockResponse({}, 404)

    @patch('requests.get', side_effect=mocked_requests_get)
    def test_search_client_by_author(self, mock_get):
        """Tests if method gets a list of books written by a provided author."""

        # with patch.object(isbn_manager.requests, 'get', return_value=response) as mock_method:

        response = isbn_manager.search_by(self.filter_author, self.author)
        self.assertEqual(response.data, json.loads(open(UNIT_TEST_RESOURCES_FOLDER +
                                                   FILE_NAME_AUTHOR_SEARCH_RESPONSE).read())["data"])

    @SkipTest
    @patch('requests.get', side_effect=mocked_requests_get)
    def test_search_client_by_title(self, mock_get):
        """Tests if method gets a list of books that match with the title."""

        response = isbn_manager.search_by(self.title)
        self.assertEqual(response, json.loads(open(UNIT_TEST_RESOURCES_FOLDER +
                                                   FILE_NAME_AUTHOR_SEARCH_RESPONSE).read())["data"])

    @patch('requests.get', side_effect=mocked_requests_get)
    def test_search_client_by_isbn(self, mock_get):
        """Tests if method gets a book searching by ISBN."""

        response = isbn_manager.search_by(self.filter_isbn, self.ISBN)
        self.assertEqual(response.data, json.loads(open(UNIT_TEST_RESOURCES_FOLDER +
                                                   FILE_NAME_ISBN_SEARCH_RESPONSE).read())["data"])

    @SkipTest
    @patch('requests.get', side_effect=mocked_requests_get)
    def test_search_client_by_publisher(self, mock_get):
        """Tests if method gets a list of books that match with the publisher."""

        response = isbn_manager.search_by(self.title)
        self.assertEqual(response, json.loads(open(UNIT_TEST_RESOURCES_FOLDER +
                                                   FILE_NAME_AUTHOR_SEARCH_RESPONSE).read())["data"])

    @SkipTest
    @patch('requests.get', side_effect=mocked_requests_get)
    def test_search_client_by_topic(self, mock_get):
        """Tests if method gets a list of books that match with the topic."""

        response = isbn_manager.search_by(self.title)
        self.assertEqual(response, json.loads(open(UNIT_TEST_RESOURCES_FOLDER +
                                                   FILE_NAME_AUTHOR_SEARCH_RESPONSE).read())["data"])

    def test_load_index(self):
        """Tests if method load the index page."""
        c = Client()
        response = c.get('/taric_books/')

        self.assertEqual(response.status_code, 200)

    def test_load_taric(self):
        """Tests if method load the taric page."""
        c = Client()
        response = c.get('/taric_books/taric/')

        self.assertEqual(response.status_code, 200)

    def test_load_github(self):
        """Tests if method load the github page."""
        c = Client()
        response = c.get('/taric_books/github/')

        self.assertEqual(response.status_code, 200)

    def test_load_about(self):
        """Tests if method load the about page."""
        c = Client()
        response = c.get('/taric_books/about/')

        self.assertEqual(response.status_code, 200)

    @patch('requests.get', side_effect=mocked_requests_get)
    def test_cover_url_from_googlebooks(self, mock_get):
        """Tests if method gets a Cover url for ISBN."""
        response = gbooks_covers.find_cover_url_by_isbn(self.ISBN_for_cover)
        expected = "http://books.google.es/books/content?id=CoBGdI5WyOIC&printsec=frontcover&" \
                   "img=1&zoom=1&edge=curl&source=gbs_api"

        self.assertEqual(response, expected)
        self.assertTrue(mock_get.called)

    @patch('requests.get', side_effect=mocked_requests_get)
    def test_cover_url_from_googlebooks_no_image(self, mock_get):
        """Tests if method returns None if there is no cover found in GoogleBooks with provided ISBN."""
        response = gbooks_covers.find_cover_url_by_isbn(self.ISBN_no_cover)
        self.assertIsNone(response)
        self.assertTrue(mock_get.called)

    @patch('requests.get', side_effect=mocked_requests_get)
    def test_cover_url_from_googlebooks_no_book(self, mock_get):
        """Tests if method returns None if there is no book found in GoogleBooks with provided ISBN."""
        response = gbooks_covers.find_cover_url_by_isbn(self.ISBN_no_book_cover)
        self.assertIsNone(response)
        self.assertTrue(mock_get.called)
