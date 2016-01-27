"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
__author__ = 'Geon'

from django.test import TestCase
from mockito import *
from mock import patch, MagicMock
import isbn_manager

""" Class to test the interaction with isbndb
"""

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class isbn_client_tests(TestCase):
    def setUp(self):

        self.author = "Eduardo Mendoza"
        self.mockedClient = mock()
        # mockedCursor = MyCursor()
        # when(self.mockedClient).cursor().thenReturn(mockedCursor)

    def test_search_client(self):
        """Tests if method gets a list of books."""
        response = isbn_manager.search_by_author(self.author)
        self.assertEqual(response, 5)
