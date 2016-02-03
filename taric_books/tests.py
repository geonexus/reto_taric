"""
This file contains all tests related to taric_books project.

To tests this module you should execute
"python manage.py test taric_books" from root directory of the project reto_taric

"""
__author__ = 'Geon'

from django.test import TestCase
from django.test import Client
from models import Struct
from django.conf import settings
from mock import patch
import json
import isbn_utils
import gbooks_covers
from reto_taric.constants import UNIT_TEST_RESOURCES_FOLDER, FILE_NAME_AUTHOR_SEARCH_RESPONSE, \
     FILE_NAME_AUTHOR_SEARCH_PAGE_RESPONSE, \
    FILE_NAME_ISBN_SEARCH_RESPONSE, FILE_NAME_COVER_SEARCH_RESPONSE, FILE_NAME_COVER_SEARCH_NO_IMAGE_RESPONSE,\
    FILE_NAME_COVER_SEARCH_NO_BOOK_RESPONSE, FILE_NAME_TITLE_SEARCH_RESPONSE, FILE_NAME_PUBLISHER_SEARCH_RESPONSE, \
    FILE_NAME_SUBJECT_SEARCH_RESPONSE, FILE_NAME_SUBJECT_SEARCH_PAGE_RESPONSE
import reto_taric.wsgi as wsgi
from django.test.client import RequestFactory


class WSGITest(TestCase):
    """ Class to test the WSGI deployment
    """

    def test_get_wsgi_application(self):
        """
        Verify that ``get_wsgi_application`` returns a functioning WSGI
        callable.
        """
        application = wsgi.get_wsgi_application()

        environ = RequestFactory()._base_environ(
            PATH_INFO="/taric_books/",
            CONTENT_TYPE="text/html; charset=utf-8",
            REQUEST_METHOD="GET"
        )

        response_data = {}

        def start_response(status, headers):
            response_data["status"] = status
            response_data["headers"] = headers

        response = application(environ, start_response)

        self.assertEqual(response_data["status"], "200 OK")


class Taric_books_tests(TestCase):
    """Class to test the interaction with isbndb, googleBooks and different static locations of
    the application.
    """
    def setUp(self):
        self.author = "eduardo-mendoza"
        self.filter_author = "author_name"
        self.filter_isbn = "book"  # filtering by book includes ISBN direct search and title direct search
        self.filter_title = "title"
        self.filter_publisher = "publisher_name"
        self.filter_subject = "subject"

        self.title = "rina-de-gatos"
        self.ISBN = "9788408105626"
        self.ISBN_for_cover = "9788432291395"
        self.ISBN_no_cover = "9781582346816"
        self.ISBN_no_book_cover = "0000000000000"
        self.subject = "computer-science"
        self.publisher = "salamandra"

    def mocked_requests_get(*args, **kwargs):
        """ mocked_requests_get defines all mocked responses when a requests is performed.
        """
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data

        query_author = "books?q=" + "eduardo-mendoza" + "&i=" + "author_name"
        query_title = "books?q=" + "rina-de-gatos" + "&i=" + "title"
        query_publisher = "books?q=" + "salamandra" + "&i=" + "publisher_name"

        query_subject = "subjects?q=" + "computer-science"
        query_subject_page = "subjects?q=" + "computer-science" + "&p=2"
        query_author_page = "books?q=" + "eduardo-mendoza" + "&i=" + "author_name" + "&p=2"
        query_isbn = "book/" + "9788408105626"
        ISBN_with_cover = "9788432291395"
        ISBN_without_cover = "9781582346816"
        ISBN_no_book_cover = "0000000000000"

        if args[0] == settings.ISBNDB_API_URL + query_author:
            return MockResponse(json.loads(open(UNIT_TEST_RESOURCES_FOLDER +
                                                FILE_NAME_AUTHOR_SEARCH_RESPONSE).read()), 200)
        elif args[0] == settings.ISBNDB_API_URL + query_author_page:
            return MockResponse(json.loads(open(UNIT_TEST_RESOURCES_FOLDER +
                                                FILE_NAME_AUTHOR_SEARCH_PAGE_RESPONSE).read()), 200)
        elif args[0] == settings.ISBNDB_API_URL + query_isbn:
            return MockResponse(json.loads(open(UNIT_TEST_RESOURCES_FOLDER +
                                                FILE_NAME_ISBN_SEARCH_RESPONSE).read()), 200)
        elif args[0] == settings.ISBNDB_API_URL + query_title:
            return MockResponse(json.loads(open(UNIT_TEST_RESOURCES_FOLDER +
                                                FILE_NAME_TITLE_SEARCH_RESPONSE).read()), 200)
        elif args[0] == settings.ISBNDB_API_URL + query_publisher:
            return MockResponse(json.loads(open(UNIT_TEST_RESOURCES_FOLDER +
                                                FILE_NAME_PUBLISHER_SEARCH_RESPONSE).read()), 200)
        elif args[0] == settings.ISBNDB_API_URL + query_subject:
            return MockResponse(json.loads(open(UNIT_TEST_RESOURCES_FOLDER +
                                                FILE_NAME_SUBJECT_SEARCH_RESPONSE).read()), 200)
        elif args[0] == settings.ISBNDB_API_URL + query_subject_page:
            return MockResponse(json.loads(open(UNIT_TEST_RESOURCES_FOLDER +
                                                FILE_NAME_SUBJECT_SEARCH_PAGE_RESPONSE).read()), 200)
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

        response = isbn_utils.search_by(self.filter_author, self.author)
        self.assertEqual(response.data, json.loads(open(UNIT_TEST_RESOURCES_FOLDER +
                                                   FILE_NAME_AUTHOR_SEARCH_RESPONSE).read())["data"])

    @patch('requests.get', side_effect=mocked_requests_get)
    def test_search_client_by_author_page2(self, mock_get):
        """Tests if method gets the page 2 of books list written by a provided author."""

        response = isbn_utils.search_by(self.filter_author, self.author, page="2")
        self.assertEqual(response.data, json.loads(open(UNIT_TEST_RESOURCES_FOLDER +
                                                   FILE_NAME_AUTHOR_SEARCH_PAGE_RESPONSE).read())["data"])

    @patch('requests.get', side_effect=mocked_requests_get)
    def test_search_client_by_title(self, mock_get):
        """Tests if method gets a list of books that match with the title."""

        response = isbn_utils.search_by(self.filter_title, self.title)
        self.assertEqual(response.data, json.loads(open(UNIT_TEST_RESOURCES_FOLDER +
                                                   FILE_NAME_TITLE_SEARCH_RESPONSE).read())["data"])

    @patch('requests.get', side_effect=mocked_requests_get)
    def test_search_client_by_isbn(self, mock_get):
        """Tests if method gets a book searching by ISBN."""

        response = isbn_utils.search_by(self.filter_isbn, self.ISBN)
        self.assertEqual(response.data, json.loads(open(UNIT_TEST_RESOURCES_FOLDER +
                                                   FILE_NAME_ISBN_SEARCH_RESPONSE).read())["data"])

    @patch('requests.get', side_effect=mocked_requests_get)
    def test_search_client_by_publisher(self, mock_get):
        """Tests if method gets a list of books that match with the publisher."""

        response = isbn_utils.search_by(self.filter_publisher, self.publisher)
        self.assertEqual(response.data, json.loads(open(UNIT_TEST_RESOURCES_FOLDER +
                                                   FILE_NAME_PUBLISHER_SEARCH_RESPONSE).read())["data"])

    @patch('requests.get', side_effect=mocked_requests_get)
    def test_search_client_by_subject(self, mock_get):
        """Tests if method gets a list of books that match with the subject."""

        response = isbn_utils.search_by(self.filter_subject, self.subject)
        self.assertEqual(response.data, json.loads(open(UNIT_TEST_RESOURCES_FOLDER +
                                                   FILE_NAME_SUBJECT_SEARCH_RESPONSE).read())["data"])

    @patch('requests.get', side_effect=mocked_requests_get)
    def test_search_client_by_subject_page2(self, mock_get):
        """Tests if method gets the page 2 of a list of books that match with the subject."""

        response = isbn_utils.search_by(self.filter_subject, self.subject, page="2")
        self.assertEqual(response.data, json.loads(open(UNIT_TEST_RESOURCES_FOLDER +
                                                   FILE_NAME_SUBJECT_SEARCH_PAGE_RESPONSE).read())["data"])

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

    def test_load_unknow_page(self):
        """Tests if returns an error page when tries to get an unknown endpoint."""

        c = Client()
        response = c.get('/unknown_page/')

        self.assertEqual(response.status_code, 404)

    @patch('requests.get', side_effect=mocked_requests_get)
    def test_load_search(self, mock_get):
        """Tests if method load the search web when I perform a search by title."""

        c = Client()
        data = {
            'search_type': self.filter_title,
            'search_value': self.title
        }
        response = c.post('/taric_books/search/', data=data)

        self.assertEqual(response.status_code, 200)

    @patch('requests.get', side_effect=mocked_requests_get)
    def test_load_search_page(self, mock_get):
        """Tests if method load the second page of search web when I perform a search by author."""

        c = Client()
        data = {
            'search_type': self.filter_author,
            'search_value': self.author,
            'page_value': '2'
        }
        response = c.post('/taric_books/search_page/'
                          + self.author + '/' + self.filter_author + '/', data=data)

        self.assertEqual(response.status_code, 200)

    @patch('requests.get', side_effect=mocked_requests_get)
    def test_load_search_subject(self, mock_get):
        """Tests if method load the search web when I perform a search by subject."""

        c = Client()
        data = {
            'search_type': self.filter_subject,
            'search_value': self.subject,
        }
        response = c.post('/taric_books/search/', data=data)

        self.assertEqual(response.status_code, 200)

    @patch('requests.get', side_effect=mocked_requests_get)
    def test_load_search_subject_page2(self, mock_get):
        """Tests if method load the second page of search web when I perform a search by subject."""

        c = Client()
        data = {
            'search_type': self.filter_subject,
            'search_value': self.subject,
            'page_value': '2'

        }
        response = c.post('/taric_books/search_page/'
                          + self.subject + '/' + self.filter_subject + '/', data=data)

        self.assertEqual(response.status_code, 200)

    @patch('requests.get', side_effect=mocked_requests_get)
    def test_load_book_details(self, mock_get):
        """Tests if method load the details web with book details about a single book
        providing the ISBN of the book."""

        c = Client()
        data = {
            'search_type': self.filter_subject,
            'search_value': self.subject,
        }
        response = c.get('/taric_books/%s/' % self.ISBN)

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


class Taric_books_model_tests(TestCase):
    """Class to test models from taric_books application.
    """
    def test_Struct(self):
        """Tests if class Struct returns an Object from a dictionary"""

        my_dict = {'param1': 'value1', 'param2': {'param21': 'value21'}}
        object1 = Struct(my_dict)

        self.assertEqual(my_dict["param1"], object1.param1)
