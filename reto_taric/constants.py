__author__ = 'Geon'

APP_TITLE = u'Taric Books'
BUTTON_SEARCH_TEXT = u"Search books"


# Unit tests constants
UNIT_TEST_RESOURCES_FOLDER = u'taric_books/test_resources/'
FILE_NAME_AUTHOR_SEARCH_RESPONSE = u'author_search_response_text.json'
FILE_NAME_AUTHOR_SEARCH_PAGE_RESPONSE = u'author_search_response_page_text.json'
FILE_NAME_TITLE_SEARCH_RESPONSE = u'title_search_response_text.json'
FILE_NAME_PUBLISHER_SEARCH_RESPONSE = u'publisher_search_response_text.json'
FILE_NAME_SUBJECT_SEARCH_RESPONSE = u'subject_search_response_text.json'
FILE_NAME_SUBJECT_SEARCH_PAGE_RESPONSE = u'subject_search_response_page_text.json'
FILE_NAME_ISBN_SEARCH_RESPONSE = u'isbn_search_response_text.json'
FILE_NAME_COVER_SEARCH_RESPONSE = u'cover_search_with_image.json'
FILE_NAME_COVER_SEARCH_NO_IMAGE_RESPONSE = u'cover_search_without_image.json'
FILE_NAME_COVER_SEARCH_NO_BOOK_RESPONSE = u'cover_search_not_found.json'

SEARCH_TYPES = (
    ('title', 'Title'),
    ('author_name', 'Author'),
    ('isbn', 'ISBN13'),
    ('publisher_name', 'Publisher'),
    ('subject', 'Subject'),
)
