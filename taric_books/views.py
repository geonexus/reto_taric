from django.shortcuts import render
from django.utils.text import slugify
from .forms import SearchFormType, SearchFormValue, PageForm
import isbn_utils
import gbooks_covers


def index(request):
    """Main View for the starting page where the search form is shown.

    :param request: The http request
    :return: a render of the given HTML page.
    """

    form_type = SearchFormType()
    form_value = SearchFormValue()
    return render(request, 'taric_books/index.html', {'form_type': form_type, 'form_value': form_value})


def search(request):
    """View to render the page where search results will be displayed.

    :param request: The http request
    :return: a render of the given HTML page.
    """

    form = PageForm()
    search_value = slugify(request.POST['search_value'])
    search_type = request.POST['search_type']

    if search_value == "":
        form_type = SearchFormType()
        form_value = SearchFormValue()
        return render(request, 'taric_books/index.html', {'form_type': form_type, 'form_value': form_value})

    response = isbn_utils.search_by(search_type, search_value, page=None)
    if search_type == "subject":
        html_template = "search_subject_result.html"
    else:
        html_template = "search_result.html"
    context = {
        'page_form': form,
        'data_list': response.data,
        'page_count': response.page_count,
        'current_page': response.current_page,
        'next_page': int(response.current_page) + 1,
        'search_value': search_value,
        'search_type': search_type
    }

    return render(request, 'taric_books/' + html_template, context)


def search_page(request, search, search_type):
    """View to render a different Page result than the first, where search results will be displayed.

    :param request: The http request
    :return: a render of the given HTML page.
    """

    form = PageForm()
    search_value = slugify(search)
    page = request.POST['page_value']

    response = isbn_utils.search_by(search_type, search_value, page=page)
    if search_type == "subject":
        html_template = "search_subject_result.html"
    else:
        html_template = "search_result.html"
    context = {
        'page_form': form,
        'data_list': response.data,
        'page_count': response.page_count,
        'current_page': response.current_page,
        'next_page': int(response.current_page) + 1,
        'search_value': search_value,
        'search_type': search_type
    }

    return render(request, 'taric_books/' + html_template, context)


def isbn(request, value):
    """View to render the information about a single book details, including its cover if it is available.
    Books could be found by ISBN or internal book_id according to ISBNdb API.

    :param request: The http request
    :return: a render of the given HTML page.
    """
    # filtering by "book" includes ISBN direct search and title direct search
    response = isbn_utils.search_by("book", value)
    isbn13 = response.data[0]["isbn13"]
    cover_url = gbooks_covers.find_cover_url_by_isbn(isbn13)
    context = {
        'book_details': response.data,
        'cover_url': cover_url,
    }

    return render(request, 'taric_books/isbn.html', context)


def taric(request):
    """View to render a web page with a link to Taric's web Page.

    :param request: The http request
    :return: a render of the given HTML page.
    """

    return render(request, 'taric_books/taric.html')


def github(request):
    """View to render a web page with a link to Github's project page.

    :param request: The http request
    :return: a render of the given HTML page.
    """

    return render(request, 'taric_books/github.html')


def about(request):
    """View to render a web page describing what is this project.

    :param request: The http request
    :return: a render of the given HTML page.
    """

    return render(request, 'taric_books/about.html')
