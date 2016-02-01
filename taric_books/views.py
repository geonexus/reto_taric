from django.http import HttpResponse
from django.shortcuts import render
from django.utils.text import slugify
from django.conf import settings
from .forms import SearchFormType, SearchFormValue, PageForm
import isbn_manager
import gbooks_covers


def index(request):
    form_type = SearchFormType()
    form_value = SearchFormValue()
    return render(request, 'taric_books/index.html', {'form_type': form_type, 'form_value': form_value})


def search(request):
    form = PageForm()
    search_value = slugify(request.POST['search_value'])
    search_type = request.POST['search_type']

    if search_value == "":
        form_type = SearchFormType()
        form_value = SearchFormValue()
        return render(request, 'taric_books/index.html', {'form_type': form_type, 'form_value': form_value})

    response = isbn_manager.search_by(search_type, search_value, page=None)
    print response
    context = {
        'page_form': form,
        'books_list': response.data,
        'page_count': response.page_count,
        'current_page': response.current_page,
        'next_page': int(response.current_page) + 1,
        'search_value': search_value,
        'search_type': search_type
    }

    return render(request, 'taric_books/search_result.html', context)


def search_page(request, search, search_type):
    form = PageForm()
    search_value = slugify(search)
    page = request.POST['page_value']
    response = isbn_manager.search_by(search_type, search_value, page=page)
    context = {
        'page_form': form,
        'books_list': response.data,
        'page_count': response.page_count,
        'current_page': response.current_page,
        'next_page': int(response.current_page) + 1,
        'search_value': search_value,
        'search_type': search_type
    }

    return render(request, 'taric_books/search_result.html', context)


def isbn(request, isbn):
    response = isbn_manager.search_by("ISBN", isbn)
    cover_url = gbooks_covers.find_cover_url_by_isbn(isbn)
    context = {
        'book_details': response.data,
        'cover_url': cover_url,
    }

    return render(request, 'taric_books/isbn.html', context)


def taric(request):
    return render(request, 'taric_books/taric.html')


def github(request):
    return render(request, 'taric_books/github.html')


def about(request):
    return render(request, 'taric_books/about.html')
